import subprocess

def change_ip(new_ip):
    try:
        # Windows uchun
        subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'address', 'name="Ethernet"', 'static', new_ip, '255.255.255.0', '192.168.1.1'], check=True)
        
        # Linux uchun (ifconfig)
        # subprocess.run(['sudo', 'ifconfig', 'eth0', 'down'], check=True)
        # subprocess.run(['sudo', 'ifconfig', 'eth0', '192.168.1.2', 'netmask', '255.255.255.0', 'up'], check=True)
        
        print(f"IP manzil o'zgartirildi: {new_ip}")
    except subprocess.CalledProcessError as e:
        print(f"Xatolik yuz berdi: {e}")

# Yangi IP manzilini o'zgartirish
new_ip_address = '192.168.1.2'
change_ip(new_ip_address)
