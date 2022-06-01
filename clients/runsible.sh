#!/bin/bash

ansible-playbook -i webservice, config_webservice_host.yml 

#Optional: --ssh-common-args '-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null'