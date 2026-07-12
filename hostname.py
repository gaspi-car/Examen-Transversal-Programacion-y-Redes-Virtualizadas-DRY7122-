
from ncclient import manager
import xml.dom.minidom

HOST = "192.168.56.105"
PORT = 830
USER = "cisco"
PASS = "cisco123!"

NUEVO_HOSTNAME = "AVALOS-PINTO"

m = manager.connect(
    host=HOST,
    port=PORT,
    username=USER,
    password=PASS,
    hostkey_verify=False
)

print("Conexion NETCONF establecida correctamente con el CSR1000v.\n")

config_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>{0}</hostname>
  </native>
</config>
""".format(NUEVO_HOSTNAME)

respuesta = m.edit_config(target="running", config=config_hostname)
print("Cambio de hostname:")
print(xml.dom.minidom.parseString(respuesta.xml).toprettyxml())

# 2. Crear la interfaz Loopback11
config_loopback = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>11</name>
        <description>Loopback creada via NETCONF - Item 4</description>
        <ip>
          <address>
            <primary>
              <address>11.11.11.11</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

respuesta = m.edit_config(target="running", config=config_loopback)
print("Creacion de Loopback11:")
print(xml.dom.minidom.parseString(respuesta.xml).toprettyxml())

m.close_session()
print("\nSesion NETCONF cerrada.")
