from lxml import etree
from lxml import html


class Professor:
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.middlen = ''
        self.number = []
        self.interests = []
        self.email = []
        self.jobs = ''


def teachers_with_xpath(f):
    root = html.fromstring(f)
    persons = root.xpath('//div[@class="post person"]')  # массив со всеми сотрудниками
    x_path_profs = []
    for prep in persons:
        person = Professor()
        number = prep.xpath('.//div[@class="l-extra small"]//span/text()')
        person.number = number
        name = prep.xpath('.//a[@class = "link link_dark large b"]/text()')
        name_new = name[1].split()

        if len(name_new) > 2:
            person.surname = name_new[0].strip()
            person.name = name_new[1].strip()
            person.middlen = name_new[2].strip()
        else:
            person.surname = name_new[0].strip()
            person.name = name_new[1].strip()
            person.middlen = ''
        interests = prep.xpath('.//a[contains(@class, "tag")]/text()')
        person.interests = interests
        email = prep.xpath('.//div[@class="l-extra small"]//a[@class="link"]/text()')
        person.email = email
        positions = prep.xpath('.//p[@class="with-indent7"]//span')
        jobs = dict()
        for p in positions:
            places = p.xpath('.//a[@class = "link"]/text()')
            places = ' / '.join(places)
            p.text = p.text.strip()
            places = places.strip()
            jobs[p.text] = places
        person.jobs = jobs

        x_path_profs.append(person)
    return x_path_profs


def teachers_with_etree(f):
    root = etree.HTML(f)
    etree_profs = []
    persons = root[1][1][3][2][1][0][2][1]
    for person in persons:
        if 'post person' in person.attrib['class']:
            teacher = Professor()
            for elem in person[0]:
                if 'l-extra small' in elem.attrib['class']:
                    extra_small = elem
                    for tag in extra_small:
                        if tag.tag == 'span':
                            teacher.number.append(tag.text)
                        elif tag.tag == 'a':
                            teacher.email.append(tag.text)

                elif 'main content small' in elem.attrib['class']:
                    main_cont = elem
                    name = main_cont[0][0][0]
                    all_name = name.attrib['title'].split()
                    if len(all_name) > 2:
                        teacher.surname = all_name[0]
                        teacher.name = all_name[1]
                        teacher.middlen = all_name[2]
                    else:
                        teacher.surname = all_name[0]
                        teacher.name = all_name[1]
                        teacher.middlen = ''
                    job = main_cont[0][1]
                    jobs = dict()
                    for tag in job:
                        if tag.tag == 'span':
                            position = tag.text
                            places = []
                            for child in tag:
                                if child.tag == 'a':
                                    places.append(child.text)
                            places = ' / '.join(places)
                            jobs[position.strip()] = places
                    teacher.jobs = jobs

                    for tag in main_cont[0]:
                        if 'with-indent small' in tag.attrib['class']:
                            for child in tag:
                                if child.tag == 'a':
                                    teacher.interests.append(child.text)
            etree_profs.append(teacher)
    return etree_profs


def main():
    with open('preps.html', 'r', encoding='utf-8') as page:
        f = page.read()

    # a = teachers_with_etree(f)
    a = teachers_with_xpath(f)
    print(a[24].name)
    print(a[24].surname)
    print(a[24].middlen)
    print(a[24].jobs)
    print(a[24].email)
    print(a[24].number)
    print(a[24].interests)


if __name__ == '__main__':
    main()
