# from __future__ import unicode_literals

import csv
import sys
import os

from django.conf import settings

project_path = "/Users/miquel/UN/0003-CRPTDEV/contacts/"
sys.path.append(project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.contrib.auth.models import User

from contactsapp.models import Contact, Tag


def load_contacts_file():
    """
    Function to load contacts from contacts.csv file
    :return:
    """
    print("load_users_file. Start.")
    file_path = settings.BASE_DIR + "/contacts/files/contacts.csv"
    data_reader = csv.reader(open(file_path), delimiter=";", quotechar='"')
    for row in data_reader:
        try:
            # read data from line
            name = row[0].strip()
            first_name = row[1].strip()
            last_name = row[2].strip()
            organization = row[3].strip()
            position = row[4].strip()
            email1 = row[5].strip()
            email2 = row[6].strip()
            telephone1 = row[7].strip()
            mobile1 = row[8].strip()
            mobile2 = row[9].strip()
            country = row[10].strip()
            state = row[11].strip()
            city = row[12].strip()
            street = row[13].strip()
            zip_code = row[14].strip()
            website = row[15].strip()
            # create contact
            contact = Contact()
            contact.name = name
            contact.first_name = first_name
            contact.last_name = last_name
            contact.organization = organization
            contact.position = position
            contact.email1 = email1
            contact.email2 = email2
            contact.telephone1 = telephone1
            contact.mobile1 = mobile1
            contact.mobile2 = mobile2
            contact.country = country
            contact.state = state
            contact.city = city
            contact.street = street
            contact.zip_code = zip_code
            contact.website = website
            try:
                contact.save()
            except:
                print("Saving value: " + row[1].strip())
                print("Unexpected error:", sys.exc_info())
        except:
            print("Saving value: " + format(row))
            print("Unexpected error:", sys.exc_info())
    print("load_users_file. End.")


def load_users_file():
    """
    Function to load users from users.csv file
    :return:
    """
    print("load_users_file. Start.")
    file_path = settings.BASE_DIR + "/contacts/files/users.csv"
    data_reader = csv.reader(open(file_path), delimiter=";", quotechar='"')
    for row in data_reader:
        try:
            # read data from line
            name = row[0].strip()
            first_name = row[1].strip()
            last_name = row[2].strip()
            email = row[3].strip()
            # create user
            user = User.objects.create_user(name, email, 'crpp2013')
            user.last_name = last_name
            #user.groups.add()
            try:
                user.save()
            except:
                print("Saving value: " + row[1].strip())
                print("Unexpected error:", sys.exc_info())
        except:
            print("Saving value: " + format(row))
            print("Unexpected error:", sys.exc_info())
    print("load_users_file. End.")


def load_tags_file():
    print("load_tags_file. Start.")
    file_path = settings.BASE_DIR + "/contacts/files/tags.csv"
    data_reader = csv.reader(open(file_path), delimiter=";", quotechar='"')
    for row in data_reader:
        try:
            # read data from line
            my_tag = row[0].strip()
            # create tag
            tag = Tag()
            tag.name = my_tag
            try:
                tag.save()
            except:
                print("Saving value: " + row[0].strip())
                print("Unexpected error:", sys.exc_info())
        except:
            print("Saving value: " + format(row))
            print("Unexpected error:", sys.exc_info())
    print("load_tags_file. End.")


if __name__ == "__main__":
    load_users_file()
    load_tags_file()
    load_contacts_file()