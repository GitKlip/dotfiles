#!/bin/bash

#PROD

# add ssh keys to chain
ssh-add -k ~/.ssh/authorized_keys/devgitlabrunner.pem
ssh-add -k ~/.ssh/authorized_keys/bastion-default.pem
ssh-add -k ~/.ssh/authorized_keys/msk-prod.pem

# connect to the bastion box (with -A, ssh-agent forwarding)
ssh  -A centos@18.222.115.34

# (from jump box to aws box):
# ssh ec2-user@10.0.103.174
