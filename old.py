ef googleSearch(queries, output_mode,tld):
    result=[]
    #Run queries.
    if(output_mode == "-t"):
        for query in queries:
            print("Running query: "+query + tld)
            time.sleep(5)
            print("Waiting to avoid bot detection...")
            browser.get("https://www.google.com/search?q="+query+ tld)
            found_url_divs=browser.find_elements_by_class_name("r")
            found_description_divs=browser.find_elements_by_class_name("s")
            for url in found_url_divs:
                links=url.find_elements_by_tag_name("a")
                for link in links:
                    result.append(link.get_attribute("href"))
                for description in found_description_divs:
                    result.append(description.text)
    elif(output_mode == "-c"):
        for query in queries:
            print("Running query: " + query + tld)
            time.sleep(5)
            print("Waiting to avoid bot detection...")
            browser.get("https://google.com/search?q="+query + tld)
            found_divs=browser.find_elements_by_class_name("rc")
            for div in found_divs:
                result.append(div.text)
    elif(output_mode == "-f"):
        for query in queries:
            print("Running query: " + query + tld)
            time.sleep(5)
            print("Waiting to avoid bot detection...")
            browser.get("https://google.com/search?q="+query + tld)
            found_divs=browser.find_elements_by_class_name("rc")
            for div in found_divs:
                result.append(div.text)
            f = open("results.txt", "w", encoding='utf-8')
            f.write("".join(result))
            f.close()
    else:
        print("Not a valid output mode. Output modes are -c, -t, and -f.")
    print("".join(result))
