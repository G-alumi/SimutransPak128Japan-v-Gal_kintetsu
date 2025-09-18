import json
from datetime import datetime, timezone, timedelta
from jinja2 import Environment, FileSystemLoader

repo = None
with open("./repo.json", encoding="utf8") as f:
	repo = json.load(f)

repo["updates"][0]["date"] = datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d")
with open("./repo.json", "w", encoding="utf8") as f:
	json.dump(repo, f, indent=2, ensure_ascii=False)



readme = None
with open("./code/release/readme.md.tpl", encoding="utf8") as f:
	readme = f.read()

readme = readme.replace(
	"<!-- updateHistory -->",
	f'<!-- updateHistory -->\n### {repo["updates"][0]["tag"]}\n{repo["updates"][0]["description"]}\n'
)
with open("./code/release/readme.md.tpl", "w", encoding="utf8") as f:
	f.write(readme)



env = Environment(loader=FileSystemLoader("./code/release", encoding="utf-8"))
tpl = env.get_template("readme.md.tpl")
with open("./readme.md", "w", encoding="utf8") as f:
	f.write(tpl.render(repo))
