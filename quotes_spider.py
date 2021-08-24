import scrapy
from scrapy import Request

#<!----------------- Scraping Owler ---------------!>
# class QuoteSpider(scrapy.Spider):
#   name= 'owler'
#   start_urls = [
#     'https://corp.owler.com/'
#   ]

#   def parse(self, response):
#     all_companies = response.css('#top-companies-on-owler a::attr(href)').getall()
#     for company in all_companies:
#       link = response.urljoin(company)
#       yield Request(url=link, callback = self.parse_profile)

#   def parse_profile(self,response):
#     ceo = response.css('.name::text').get()
#     revenue = response.css('.botifyrevenuedata::text').get()
#     sic_code = response.css('.black-deeplink::text').get()
#     employee_strength = response.css('.botifyemployeedata::text').get()
#     sector = response.css('.sectors .deeplink::text').get()

#     item = {
#       'Name of CEO': ceo,
#       'Annual Revenue': revenue,
#       'SIC Code': sic_code,
#       'No. of Employees': employee_strength,
#       'Sector': sector
#     }

#     yield item


    
    # for detail in response.css('table > tbody > tr'):
    #   comp_name = detail.css('td:nth-child(2) a::text').getall()
    #   investor = detail.css('td:nth-child(5) a::text').getall()
    #   amount = detail.css('td:nth-child(6)::text').getall()
    #   close_date = detail.css('td:nth-child(3)::text').getall()
    #   item = {
    #     'Company Name':comp_name,
    #     'Investor':investor,
    #     'Amount':amount,
    #     'Close Date':close_date,
    #   }
    #   yield item
      
#<!---------------- DealBook Code --------------------!>

# class QuoteSpider(scrapy.Spider):
#   name = 'brazilcomp'
#   page_number = 2
#   start_urls = [
#     'https://dealbook.co/deals'
#   ]

#   def parse(self, response):
#     for detail in response.css('table > tbody > tr'):
#       comp_name = detail.css('td:nth-child(2) a::text').getall()
#       investor = detail.css('td:nth-child(5) a::text').getall()
#       amount = detail.css('td:nth-child(6)::text').getall()
#       close_date = detail.css('td:nth-child(3)::text').getall()
#       item = {
#         'Company Name':comp_name,
#         'Investor':investor,
#         'Amount':amount,
#         'Close Date':close_date,
#       }
#       yield item
      
#       next_page = 'https://dealbook.co/deals?page=' + str(QuoteSpider.page_number)
#       if QuoteSpider.page_number <= 170:
#         QuoteSpider.page_number+=1
#         yield response.follow(next_page, callback = self.parse)

#----------------------------------------
#------------ Getting the investor name from the table 
# class QuoteSpider(scrapy.Spider):
#   name = 'brazilcomp'
#   page_number = 2
#   start_urls = [
#     'https://dealbook.co/investors'
#   ]

#   def parse(self, response):
#     for detail in response.css('table > tbody > tr'):
#       investor_name = detail.css('td:nth-child(2)::text').getall()
#       no_of_deals = detail.css('td:nth-child(3)::text').getall()
#       location = detail.css('.column-location::text').getall()
#       investor_type = detail.css('.column-location+ td::text').getall()
#       link_to_page = detail.css('td > a::attr(href)').getall()
#       link = response.urljoin(link_to_page[detail])
#       yield scrapy.Request(link, callback=self.parse_details)
#       item = {
#         'Investor Name':investor_name,
#         'Number of deals':no_of_deals,
#         'Location':location,
#         'Investor Type':investor_type,
#       }
#       yield item
      
#       next_page = 'https://dealbook.co/investors?page=' + str(QuoteSpider.page_number)
#       if QuoteSpider.page_number <= 170:
#         QuoteSpider.page_number+=1
#         yield response.follow(next_page, callback = self.parse)

  
#   def parse_details(self,response):
#     dict = {
#       'Investments': response.css('.item:nth-child(1) h3::text').getall(),
#       'Organizations': response.css('td:nth-child(2) a::text').getall(),
#       'Funds Raised': response.css('.item~ .item+ .item h3::text').getall(),      
#       'investment date': response.css('.table strong::text').getall(), 
#       'site': response.css('li:nth-child(1) strong a:text').getall(),
#     }
#     yield dict

#--------------------------------------------------
#---------- Going inside each investor to get details-----------
# class QuoteSpider(scrapy.Spider):
#   name = 'brazilcomp'
#   page_number = 2
#   start_urls = [
#     'https://dealbook.co/investors'
#   ]

#   def parse(self, response):
#     a = response.css('table>tbody>tr>td a::attr(href)').getall()
#     for link in a:
#       link = response.urljoin(link)
#       yield scrapy.Request(link, callback=self.parse_details)

#       next_page = 'https://dealbook.co/investors?page=' + str(QuoteSpider.page_number)
#       if QuoteSpider.page_number <= 170:
#          QuoteSpider.page_number+=1
#          yield response.follow(next_page, callback = self.parse)

  
#   def parse_details(self,response):
#     c = response.css('.tag::text').getall()
#     for i in c:
#       i = i.strip()
#     dict = {
#       'Investor Name': response.css('.status-name h1::text').getall(),
#       'Investor Type': i,
#       'Investments': response.css('.item:nth-child(1) h3::text').getall(),
#       'Organizations': response.css('td:nth-child(2) a::text').getall(),
#       'Funds Raised': response.css('.item~ .item+ .item h3::text').getall(),      
#       'investment date': response.css('.table strong::text').getall(), 
#       'site': response.css('.info-contact>li>p>a::attr(href)').getall(),
#     }
#     yield dict

# class QuoteSpider(scrapy.Spider):
#   name = 'brazilcomp'
#   page_number = 2
#   start_urls = [
#     'https://dealbook.co/companies'
#   ]

#   def parse(self, response):
#     for detail in response.css('table > tbody > tr'):
#       organization = detail.css('td:nth-child(2)::text').getall()
#       location = detail.css('.column-location::text').getall()
#       Amount_raised = detail.css('td:nth-child(6)::text').getall()
#       Deals = detail.css('.column-location+ td::text').getall()
#       item = {
#         'Organization': organization,
#         'Amount Raised':Amount_raised,
#         'Location':location,
#         'Deals':Deals,
#       }
#       yield item
      
#       next_page = 'https://dealbook.co/companies?page=' + str(QuoteSpider.page_number)
#       if QuoteSpider.page_number <= 240:
#         QuoteSpider.page_number+=1
#         yield response.follow(next_page, callback = self.parse)

class QuoteSpider(scrapy.Spider):
  name = 'brazilcomp'
  page_number = 2
  start_urls = [
    'https://dealbook.co/companies'
  ]

  def parse(self, response):
    a = response.css('table>tbody>tr>td a::attr(href)').getall()
    for link in a:
      link = response.urljoin(link)
      yield scrapy.Request(link, callback=self.parse_details)

      next_page = 'https://dealbook.co/companies?page=' + str(QuoteSpider.page_number)
      if QuoteSpider.page_number <= 240:
         QuoteSpider.page_number+=1
         yield response.follow(next_page, callback = self.parse)

  
  def parse_details(self,response):
    # c = response.css('.tag::text').getall()
    # for i in c:
    #   i = i.strip()
    dict = {
      'Deal Type': response.css('.table-responsive:nth-child(2) td:nth-child(3)').getall(),
      'Email': response.css('li~ li+ li p::text'),     
      'investment date': response.css('.table-responsive:nth-child(2) strong::text').getall(), 
      'site': response.css('.info-web-location a::attr(href)').getall(),
    }
    yield dict
  

