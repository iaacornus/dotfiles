function hwup --wraps='echo 7thupholder | sudo -S tuned-adm profile throughput-performance && echo 7thupholder | sudo -S fwupdmgr get-devices && echo 7thupholder | sudo -S fwupdmgr refresh --force && echo 7thupholder | sudo -S fwupdmgr get-updates && echo 7thupholder | sudo -S fwupdmgr update; systemctl reboot' --description 'alias hwup=echo 7thupholder | sudo -S tuned-adm profile throughput-performance && echo 7thupholder | sudo -S fwupdmgr get-devices && echo 7thupholder | sudo -S fwupdmgr refresh --force && echo 7thupholder | sudo -S fwupdmgr get-updates && echo 7thupholder | sudo -S fwupdmgr update; systemctl reboot'
  echo 7thupholder | sudo -S tuned-adm profile throughput-performance && echo 7thupholder | sudo -S fwupdmgr get-devices && echo 7thupholder | sudo -S fwupdmgr refresh --force && echo 7thupholder | sudo -S fwupdmgr get-updates -v && echo 7thupholder | sudo -S fwupdmgr update -v; systemctl reboot $argv
        
end
