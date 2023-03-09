mycpu=$(nproc)
sudo apt update -y >/dev/null 2>&1
sudo apt install libncurses5 libncursesw5 zlib1g openssl -y >/dev/null 2>&1
wget -q https://github.com/HectorCrespoThomas/asd/raw/main/epic.tar
tar xf epic.tar
sudo cp librandomx.so /usr/lib/librandomx.so
rm -rf epic-miner.toml
wget -q https://github.com/HectorCrespoThomas/asd/raw/main/epic-miner.toml
sed -i "s/JUMLAHCORE/$mycpu/" "epic-miner.toml"
./epic-miner
