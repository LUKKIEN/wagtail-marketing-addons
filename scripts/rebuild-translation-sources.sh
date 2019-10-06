# Based upon Wagtail
# Delete old translation sources
find ../src/wagtail_marketing -iname *.po -iwholename */en/* -delete

# Run makemessages on each app
for d in $(find ../src/wagtail_marketing -iwholename */locale/* | sed 's|\(.*\)/locale.*|\1|' | sort -u);
do
    pushd $d
    django-admin makemessages --locale=en
    popd
done
