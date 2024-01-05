extract:
    hatch --quiet run extract-nest-transactions /tmp/Fund\ transaction\ details*.html | xsv table
