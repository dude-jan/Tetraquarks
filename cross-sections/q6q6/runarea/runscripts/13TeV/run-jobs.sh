#!/bin/bash
(trap 'kill 0' SIGINT; sleep 0s && bash job_1.sh & sleep 1s && bash job_2.sh & sleep 2s && bash job_3.sh & sleep 3s && bash job_4.sh & sleep 4s && bash job_5.sh & sleep 5s && bash job_6.sh & sleep 6s && bash job_7.sh & sleep 7s && bash job_8.sh & wait)
