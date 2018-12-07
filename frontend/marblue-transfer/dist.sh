cnpm run build
sudo rm -rf /var/www/marblue_trans/*
sudo cp -r ./dist/* /var/www/marblue_trans/
sudo /etc/init.d/nginx restart
