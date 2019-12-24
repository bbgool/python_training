{
  "id": "23a3bacf-659d-4659-9448-f1dcff4a709e",
  "version": "2.0",
  "name": "TestMail",
  "url": "https://mail.ru",
  "tests": [{
    "id": "c39c3a5c-ee6c-429e-9e0e-845bfb15a4b5",
    "name": "TestMail",
    "commands": [{
      "id": "e77af745-ba90-4c98-930d-f5cd065b2841",
      "comment": "",
      "command": "open",
      "target": "/",
      "targets": [],
      "value": ""
    }, {
      "id": "87f27480-927f-4a04-a4a3-72f235fb60c3",
      "comment": "",
      "command": "setWindowSize",
      "target": "827x701",
      "targets": [],
      "value": ""
    }, {
      "id": "0d15e6de-af5f-4630-ad91-081c5740c56f",
      "comment": "",
      "command": "mouseOver",
      "target": "linkText=Леди",
      "targets": [
        ["linkText=Леди", "linkText"],
        ["name=clb644064", "name"],
        ["css=.tabs__item:nth-child(4)", "css:finder"],
        ["xpath=(//a[contains(text(),'Леди')])[2]", "xpath:link"],
        ["xpath=//a[@name='clb644064']", "xpath:attributes"],
        ["xpath=//div[@id='grid:middle']/div[2]/div[2]/div/a[4]", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '//lady.mail.ru/')]", "xpath:href"],
        ["xpath=//div[2]/div/a[4]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4002874a-4fce-4f21-bb79-7bee4b768d3d",
      "comment": "",
      "command": "mouseOut",
      "target": "linkText=Леди",
      "targets": [
        ["linkText=Леди", "linkText"],
        ["name=clb644064", "name"],
        ["css=.tabs__item:nth-child(4)", "css:finder"],
        ["xpath=(//a[contains(text(),'Леди')])[2]", "xpath:link"],
        ["xpath=//a[@name='clb644064']", "xpath:attributes"],
        ["xpath=//div[@id='grid:middle']/div[2]/div[2]/div/a[4]", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '//lady.mail.ru/')]", "xpath:href"],
        ["xpath=//div[2]/div/a[4]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "6ac52546-f1b4-4690-8025-c250e242c47b",
      "comment": "",
      "command": "click",
      "target": "id=q",
      "targets": [
        ["id=q", "id"],
        ["name=q", "name"],
        ["css=#q", "css:finder"],
        ["xpath=//input[@id='q']", "xpath:attributes"],
        ["xpath=//form[@id='search']/input[2]", "xpath:idRelative"],
        ["xpath=//input[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "18c38f88-6999-470f-9aaa-8c2fb3cfe6c0",
      "comment": "",
      "command": "type",
      "target": "id=q",
      "targets": [
        ["id=q", "id"],
        ["name=q", "name"],
        ["css=#q", "css:finder"],
        ["xpath=//input[@id='q']", "xpath:attributes"],
        ["xpath=//form[@id='search']/input[2]", "xpath:idRelative"],
        ["xpath=//input[2]", "xpath:position"]
      ],
      "value": "погода в караганде"
    }, {
      "id": "4f964847-7217-4a4f-abc5-fb81e7da5df0",
      "comment": "",
      "command": "click",
      "target": "css=.suggests__item_hover > .suggests__item__text",
      "targets": [
        ["css=.suggests__item_hover > .suggests__item__text", "css:finder"],
        ["xpath=//div[@id='suggests-list']/div[2]/span", "xpath:idRelative"],
        ["xpath=//div[2]/div/div/div[2]/span", "xpath:position"],
        ["xpath=//span[contains(.,'погода в караганде на 10 дней')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "d0758a6e-91d8-447d-bd3a-84abeb2da92e",
      "comment": "",
      "command": "close",
      "target": "",
      "targets": [],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "ed824e91-0b3b-47eb-8328-f8d99a75dee1",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["c39c3a5c-ee6c-429e-9e0e-845bfb15a4b5"]
  }],
  "urls": ["https://mail.ru/"],
  "plugins": []
}