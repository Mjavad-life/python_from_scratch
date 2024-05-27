import requests
import json
import plotly.express as px


#یک ای پی آی را میخواند و جواب را بررسی میکند
url = "https://api.github.com/search/repositories?q=language:python+sort:stars"
#url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_object = r.json()
print(f"Total repositories: {response_object['total_count']}")
print(f"Complete results: {not response_object['incomplete_results']}")
# Explore information about the repositories.
repo_dicts = response_object['items']
repo_name , stars , hover_texts , repo_links = [] , [] , [] , []
for repo_dict in repo_dicts :
    # اسم رپاسیتوری را در می آوریم
    repo_name.append(repo_dict['name'])
    # تعداد ستاره ها را استخراج میکنیم
    stars.append(repo_dict['stargazers_count'])
    #  نام هر ریپو را به لینک تبدیل میکنیم
    repo_esm = repo_dict['name']
    repo_url = repo_dict['html_url']
    # بوسیله کد اچ تی ام ال لینک درست میکند
    repo_link = f"<a href='{repo_url}'> {repo_esm} </a>"
    repo_links.append(repo_link)
    # مالک و توضیحات هر رپوز را بیرون می آوریم
    owner = repo_dict['owner']['login']
    desc = repo_dict['description']
    hover_text = f"{owner} <br /> {desc}"
    hover_texts.append(hover_text)

# چارت را میکشیم
barchasb = {'x' : 'repository' , 'y' :'stars'}
fig = px.bar(x= repo_links , y = stars , labels = barchasb , title = 'best repositoris',
             hover_name = hover_texts)
fig.write_html('repository va stareshan be sorate link .html')

#fig.show()  
