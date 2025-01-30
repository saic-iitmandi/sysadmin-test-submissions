## CHALLENGE 2- docker volume backup

(script separetly)
to be able to run this, i started by creating volumes, and containers, and mounting a few containers (not all, since we need to focus on docker mounts, so there should be some unmounted ones to be able to check).
then i wrote the script for backup/restore. it will take backup of all volumes seen on docker volume ls command
with all that done, only thing left was to write a cronjob for midnight every night
# <img align="center"  src="/q2/cronjob.png" width=500><br><br> 
done!