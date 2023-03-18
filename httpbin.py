import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
browser.open("http://httpbin.org")
browser.follow_link("forms")
browser.select_form('form[action="/post"]')
print(browser.form.print_summary())

browser["custname"] = "Best Alex"
browser["custtel"] = "+7 977 677 97 77"
browser["custemail"] = "alex@example.com"
browser["size"] = "large"
browser["topping"] = ("cheese", "bacon")
browser["comments"] = "Add more cheese, plz. More then last time!"

response = browser.submit_selected()
print(response.text)