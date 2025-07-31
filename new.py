def googleSearch(self, query):

        result = {}
        self.webdriver.get("https://google.com/search?q="+query)

        links = self.webdriver.find_elements_by_xpath("//a[@href]")
        divs  = self.webdriver.find_elements_by_tag_name("div")
        paragraphs = self.webdriver.find_elements_by_tag_name("p")

        result["Links"] = links
        result["Divs"] = divs
        result["Paragraphs"] = paragraphs

        return result
