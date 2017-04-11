import argparse
import os
import sys
import shutil
import zipfile

maven_base_package = "com" + os.path.sep + "documentum"

maven_base_pom_templ = """<?xml version="1.0" encoding="UTF-8"?>
<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd" xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <modelVersion>4.0.0</modelVersion>
  <groupId>%s</groupId>
  <artifactId>%s</artifactId>
  <version>%s</version>
  <description>POM was created by dfc.py script</description>
  %s
</project>
"""

maven_single_dep_templ = """
    <dependency>
        <groupId>%s</groupId>
        <artifactId>%s</artifactId>
        <version>%s</version>
    </dependency>
"""

parser = argparse.ArgumentParser(description='Create DFC for Maven')
parser.add_argument('dfc_jars_location', metavar='<dfc jars folder>', help='a folder containing DFC jars')
parser.add_argument('destination', metavar='<destination>', help='a destination folder')
parser.add_argument('dfc_jar', metavar='<dfc.jar path>', help='DFC jar file name, to extract the version')
parser.add_argument('--dfc_version', help='DFC version')

args = parser.parse_args()

if(args.dfc_version == None and args.dfc_jar == None):
        print("Please provide either --dfc_version or --dfc_jar")
        sys.exit(20)

if(args.dfc_version == None and args.dfc_jar != None):
    print("Extracing the DFC version")
    with zipfile.ZipFile(args.dfc_jars_location + os.path.sep + args.dfc_jar, 'r') as myzip:
        try:
            myzip.extract("DfVersion.properties", ".")

            dfc_version_file = open("DfVersion.properties", "r")
            props = dfc_version_file.readlines()
            for prop in props:
                if(prop.find('=') != -1):
                    name, value = prop.split("=", 1)
                    args.dfc_version = value.strip()
                    print("DFC version is: " + value)
                    break
            dfc_version_file.close()
            os.remove("DfVersion.properties")
        except KeyError as err:
            print("Error: " + str(err))
            print("Make sure that the " + args.dfc_jar + " is a real dfc.jar")
            sys.exit(20)

if(args.dfc_jar != None):
    jars = os.listdir(args.dfc_jars_location)
    jars = filter(lambda x: x.endswith('.jar'), jars)
    maven_base_poms = ''
    for file in jars:
        dest_path = args.destination + os.path.sep + maven_base_package + os.path.sep + file[:-4] + os.path.sep + args.dfc_version
        dest_file = file[:-4] + "-" + args.dfc_version

        try:
            os.makedirs(dest_path)
        except FileExistsError as err:
            print("Output directory already exists: " + str(err))
            # break

        shutil.copyfile(args.dfc_jars_location + os.path.sep + file, dest_path + os.path.sep + dest_file + ".jar")

        pom = maven_base_pom_templ % (maven_base_package.replace(os.path.sep, '.'), file[:-4], args.dfc_version, '')
        pom_file = open(dest_path + os.path.sep + dest_file + ".pom", 'w+')
        pom_file.write(pom);
        pom_file.close()

        maven_base_poms += maven_single_dep_templ % (maven_base_package.replace(os.path.sep, '.'), file[:-4], args.dfc_version)

    #update the dfc.pom to include dependencies

    dest_pom_path = args.destination + os.path.sep + maven_base_package + os.path.sep + args.dfc_jar[:-4] + os.path.sep + args.dfc_version
    dest_pom_file = args.dfc_jar[:-4] + "-" + args.dfc_version + ".pom"
    pom = maven_base_pom_templ % (maven_base_package.replace(os.path.sep, '.'), args.dfc_jar[:-4], args.dfc_version, '<dependencies>%s</dependencies>' % (maven_base_poms))
    pom_file = open(dest_pom_path + os.path.sep + dest_pom_file, 'w+')
    pom_file.write(pom);
    pom_file.close()

