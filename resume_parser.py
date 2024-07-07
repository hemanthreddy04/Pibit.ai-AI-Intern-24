import re
import json

def parse_resume(resume_text):
    sections = re.split(r'\n(?=[A-Za-z ]+:)', resume_text.strip())
    resume_dict = {}

    for section in sections:
        lines = section.split('\n')
        section_title = lines[0].replace(':', '')
        if section_title == "Contact Information":
            contact_info = {}
            for line in lines[1:]:
                key, value = line.split(': ', 1)
                contact_info[key] = value
            resume_dict[section_title] = contact_info
        elif section_title in ["Experience", "Education"]:
            items = []
            item = {}
            for line in lines[1:]:
                if re.match(r'^\s*-\s', line):
                    if item:
                        items.append(item)
                    item = {}
                key, value = line.split(': ', 1)
                item[key] = value
            if item:
                items.append(item)
            resume_dict[section_title] = items
        elif section_title in ["Skills", "Certifications"]:
            resume_dict[section_title] = [line.strip('- ') for line in lines[1:]]
        else:
            resume_dict[section_title] = lines[1]

    return json.dumps(resume_dict, indent=2)

resume_text = """
Contact Information:
Name: Kambham Hemanth Reddy
Phone: +91-1234567890
Email: hemanth@example.com
LinkedIn: linkedin.com/in/hemanthreddy

Summary:
Experienced professional with a track record of developing innovative solutions for project success.

Experience:
- Company: Fresh Farm Organic Food
  Role: Frontend Web Developer
  Duration: Jan 2022 - Present
  Description: Led frontend development, utilizing HTML, CSS, JavaScript, Bootstrap, and ReactJS to create a responsive website.

Education:
- Degree: Bachelor of Technology in Computer Science
  Institution: XYZ University
  Year: 2021

Skills:
- HTML
- CSS
- JavaScript
- ReactJS
- Node.js

Certifications:
- ServiceNow Micro Certification
"""

parsed_resume = parse_resume(resume_text)
print(parsed_resume)
