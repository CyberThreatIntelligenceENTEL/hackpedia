# MS17_010 Detection Tool
Esta herramienta utiliza el poder de `masscan` y `nmap` para barrer segmentos de red.

## Requerimientos
* Masscan <<https://github.com/robertdavidgraham/masscan>>
* NMap <<https://nmap.org/download.html>>
* NMap NSE <<https://github.com/cldrn/nmap-nse-scripts/blob/master/scripts/smb-vuln-ms17-010.nse>>

## Usage
```shell
sudo ./ms17_010_detect.sh example.lst
```