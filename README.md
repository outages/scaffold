# outages-scaffold

This tool is part of the [Outages Project](https://github.com/outages). It asks the user a series of question and then
generates a simple scaffolding for a tracking outages in the Outages Project format.

## Install

```bash
pip install outages-scaffold
```

## Execution

```bash
outage-scaffold
```

Answer prompts as asked.

Alternatively, parameters may be passed in:
```
$ bin/outages-scaffold --help
usage: outages-scaffold [-h] [-n SERVICE_NAME] [-t SERVICE_TYPE]
                        [-u SERVICE_URL] [-j JSON_URL]

Generate a new repository for the Outages Project

optional arguments:
  -h, --help            show this help message and exit
  -n SERVICE_NAME, --service-name SERVICE_NAME
                        Service name, one word (e.g. AWS)
  -t SERVICE_TYPE, --service-type SERVICE_TYPE
                        Service type, brief (e.g. cloud computing platform)
  -u SERVICE_URL, --service-url SERVICE_URL
                        Service url (e.g. https://aws.amazon.com)
  -j JSON_URL, --json-url JSON_URL
                        JSON url to parse (e.g.
                        https://status.aws.amazon.com/data.json)
```
