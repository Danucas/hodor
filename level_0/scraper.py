#!/usr/bin/python3
import mechanize

br = mechanize.Browser()
br.open("http://158.69.76.135/level0.php")
for i in range(4):
    br.select_form(nr=0)
    input = br.form.find_control("id")
    input.value = '1305'
    res = br.submit()
    print(i, "vote")
