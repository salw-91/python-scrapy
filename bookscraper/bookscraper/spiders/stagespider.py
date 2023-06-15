import scrapy


class StagespiderSpider(scrapy.Spider):
    name = "stagespider"
    allowed_domains = ["https://stagemarkt.nl/"]
    start_urls = ["https://stagemarkt.nl/leerbedrijven/?Termen=25604&PlaatsPostcode=ROTTERDAM&Straal=0&Land=e883076c-11d5-11d4-90d3-009027dcddb5&ZoekenIn=A&Page=1&Longitude=&Latitude=&Regio=&Plaats=&Niveau=&SBI=&Kwalificatie=&Sector=&RandomSeed=&Leerweg=&Bedrijfsgrootte=&Opleidingsgebied=&Internationaal=&Beschikbaarheid=&AlleWerkprocessenUitvoerbaar=&LeerplaatsGewijzigd=&Sortering=0&Bron=ORG&Focus=&LeerplaatsKenmerk=&OrganisatieKenmerk="]

    def parse(self, response):
        stages = response.css('a.c-link-blocks-single')

        for stage in stages:
            if  stage.css('div.c-link-blocks-single-company span::attr(onclick)').get():
                stage_web = stage.css('div.c-link-blocks-single-company span::attr(onclick)').get()[13:-2] 
            
            if 'http' in stage_web:
                yield {
                    'web': stage_web,
                }
            pass
            stage_web = 0

        next_page = response.xpath('//li[@class="is-active"]/following-sibling::li/a/@href').get()
        if next_page is not None:
            next_page_url = 'https://stagemarkt.nl' + next_page
            
            yield response.follow(next_page_url, callback=self.parse)




        

