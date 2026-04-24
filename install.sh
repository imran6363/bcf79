#!/bin/bash

clear
echo "Installing BCF79..."

pkg update -y && pkg upgrade -y
pkg install python git whois -y

pip install requests rich

# launcher create
cat > $PREFIX/bin/bcf79 << 'EOF'
#!/bin/bash

URL="https://raw.githubusercontent.com/YOUR-USERNAME/bcf79/main/bcf79.py"

curl -s -o ~/bcf79.py $URL
python ~/bcf79.py
EOF

chmod +x $PREFIX/bin/bcf79

echo "✅ Install Complete!"
echo "Run: bcf79"
