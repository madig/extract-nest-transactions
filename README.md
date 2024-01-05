# extract-nest-transactions

A tool to scrape fund transaction data out of [the ghastly NEST user interface](https://www.nestpensions.org.uk/schemeweb/NestWeb/faces/secure/FE/pages/unitStatementSearch.xhtml). Works on saved HTML pages because I don't know how to scrape the site.

Run like `hatch run extract-nest-transactions /tmp/Fund\ transaction\ details*.html | xsv table`.