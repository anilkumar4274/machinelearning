set +x
echo "###############
Downloading url
###############"

curl -s -o url1.log https://zerodha.com/margin-calculator/Equity/

echo "##################
removing html tags
##################"

sed -i -e 's/<[^>]*>//g' url1.log

echo "############################
grep for script & multiplier
############################"

egrep 'data-scrip|data-mis_multiplier' url1.log >> url2.log
mv url2.log url1.log

echo "############################################################
remove empty space before data scrip and new line after data-scrip
##############################################################"

sed -i "s/^[ \t]*//" url1.log
sed -i 'N;s/\ndata-mis_multiplier/ data-mis_multiplier/' url1.log

echo "############################################################
cutting only equity and multiplier
##############################################################"

awk -F "\"" '{ print $2,$8 }' url1.log > url2.log
mv url2.log url1.log

echo "############################################################
removing ":EQ "  from url1.log
##############################################################"

awk -F ":EQ " '{ print $1, $2 }' url1.log > url2.log
mv url2.log url1.log
sed -i 's@&@%26@g' url1.log

echo "#####################################################################
finding total num of multiplier and creating log of each individually
#####################################################################"
rm -rf temp url_*.log 
awk '{ print $2|"sort -nk2 "}' url1.log | uniq > temp
echo "#####################################################################
buying and selling quantity
#####################################################################"
rm -rf buy* sell* url_12.5.log
for j in `cat temp`
do
awk -v mul=12.5 ' { if ( $2 ~ mul ) { print $1 } }' url1.log >> url_12.5.log

IFS=$'\n'
        for i in `awk '{ print $1 }' url_12.5.log`
        do
                curl -o $i -s https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=$i
                buyquantity=$(grep -i "totalbuyquantity" $i | awk -F"totalBuyQuantity\":\"" '{ print $2 }' | awk -F\" '{ print $1 }' | sed 's/,//g' |  sed 's/-/0/g')
                sellquantity=$(grep -i "totalsellquantity" $i | awk -F"totalSellQuantity\":\"" '{ print $2 }' | awk -F\" '{ print $1 }' | sed 's/,//g' | sed 's/-/0/g')
                lastprice=$(grep -i "varMargin" $i | awk -F"lastPrice\":\"" '{ print $2 }' | awk -F\" '{ print $1 }' | sed 's/,//g' |  sed 's/-/0/g')
                percent=`expr 200 \* $buyquantity / $sellquantity % 2 + 100 \* $buyquantity / $sellquantity` 2> /dev/null
                if [ "$buyquantity" -ge "$sellquantity" ]; then
                        echo "buying quantity is greater"
                       # echo "$percent:$i" >> buy_12.5
                        calc(){ awk "BEGIN { print "$*" }"; } 2>/dev/null
                        times=`calc $buyquantity/$sellquantity`
			#times=`echo $times | awk '{ print int($1) }'`
			echo "12.5:$times:$i:$lastprice" >> buy_12.5
                else    
                        echo "selling quantity is greater"
                       # echo "$percent:$i" >> sell_12.5
                        calc(){ awk "BEGIN { print "$*" }"; } 2>/dev/null
                        times=`calc $sellquantity/$buyquantity`
			#times=`echo $times | awk '{ print int($1) }'`
			echo "12.5:$times:$i:$lastprice" >> sell_12.5
                fi      
        rm -rf $i
	done
	break
done
cat buy_* > buy
cat sell_* > sell
sort -t: -nrk2 buy > buy.1
sort -t: -nrk2 sell > sell.1
mv buy.1 buy
mv sell.1 sell
head -10 buy >> log.buy
date +"%D : %H-%M" >> log.buy
head -10 sell >> log.sell
date +"%D : %H-%M" >> log.sell
set -x
