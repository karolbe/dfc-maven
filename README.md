# dfc-maven
Creates a ready to use local Maven repository with Documentum DFC and dependencies.
Of course you will need DFC jars, I can't upload them as these are proprietary files.

Assuming you have the jars in a folder /tmp/dfc-7.2:

```
-rw-rw-rw- 1 kbryd kbryd  1034749 Jan  9  2015 castor-1.1-xml.jar
-rw-rw-rw- 1 kbryd kbryd   640394 Jan  9  2015 certj.jar
-rw-rw-rw- 1 kbryd kbryd     9207 Jan  9  2015 configservice-api.jar
-rw-rw-rw- 1 kbryd kbryd   115166 Jan  9  2015 configservice-impl.jar
-rw-rw-rw- 1 kbryd kbryd    58637 Jan  9  2015 cryptojce.jar
-rw-rw-rw- 1 kbryd kbryd  1418104 Jan  9  2015 cryptojcommon.jar
-rw-rw-rw- 1 kbryd kbryd 15301367 Jan  9  2015 dfc.jar
-rw-rw-rw- 1 kbryd kbryd     6139 Jan  9  2015 dms-client-api.jar
-rw-rw-rw- 1 kbryd kbryd   272383 Jan  9  2015 EccpressoAll.jar
-rw-rw-rw- 1 kbryd kbryd    92569 Jan  9  2015 elmjava3_1_0-jdk1.5.0_12.jar
-rw-rw-rw- 1 kbryd kbryd   201250 Jan  9  2015 flexlm.jar
-rw-rw-rw- 1 kbryd kbryd   522566 Jan  9  2015 jcmFIPS.jar
-rw-rw-rw- 1 kbryd kbryd   609905 Jan  9  2015 xtrim-api.jar
-rw-rw-rw- 1 kbryd kbryd   746154 Jan  9  2015 xtrim-server.jar
```

you run the dfc.py like this:

```
python3 dfc.py /tmp/dfc-7.2 /tmp/output-dir dfc.jar
```

this will create in /tmp/output-dir a complete folder structure compatible with Maven:

```
.
└── com
    └── documentum
        ├── castor-1.1-xml
        │   └── 7.2.0000.0054
        │       ├── castor-1.1-xml-7.2.0000.0054.jar
        │       └── castor-1.1-xml-7.2.0000.0054.pom
        ├── certj
        │   └── 7.2.0000.0054
        │       ├── certj-7.2.0000.0054.jar
        │       └── certj-7.2.0000.0054.pom
        ├── configservice-api
        │   └── 7.2.0000.0054
        │       ├── configservice-api-7.2.0000.0054.jar
        │       └── configservice-api-7.2.0000.0054.pom
        ├── configservice-impl
        │   └── 7.2.0000.0054
        │       ├── configservice-impl-7.2.0000.0054.jar
        │       └── configservice-impl-7.2.0000.0054.pom
        ├── cryptojce
        │   └── 7.2.0000.0054
        │       ├── cryptojce-7.2.0000.0054.jar
        │       └── cryptojce-7.2.0000.0054.pom
        ├── cryptojcommon
        │   └── 7.2.0000.0054
        │       ├── cryptojcommon-7.2.0000.0054.jar
        │       └── cryptojcommon-7.2.0000.0054.pom
        ├── dfc
        │   └── 7.2.0000.0054
        │       ├── dfc-7.2.0000.0054.jar
        │       └── dfc-7.2.0000.0054.pom
        ├── dms-client-api
        │   └── 7.2.0000.0054
        │       ├── dms-client-api-7.2.0000.0054.jar
        │       └── dms-client-api-7.2.0000.0054.pom
        ├── EccpressoAll
        │   └── 7.2.0000.0054
        │       ├── EccpressoAll-7.2.0000.0054.jar
        │       └── EccpressoAll-7.2.0000.0054.pom
        ├── elmjava3_1_0-jdk1.5.0_12
        │   └── 7.2.0000.0054
        │       ├── elmjava3_1_0-jdk1.5.0_12-7.2.0000.0054.jar
        │       └── elmjava3_1_0-jdk1.5.0_12-7.2.0000.0054.pom
        ├── flexlm
        │   └── 7.2.0000.0054
        │       ├── flexlm-7.2.0000.0054.jar
        │       └── flexlm-7.2.0000.0054.pom
        ├── jcmFIPS
        │   └── 7.2.0000.0054
        │       ├── jcmFIPS-7.2.0000.0054.jar
        │       └── jcmFIPS-7.2.0000.0054.pom
        ├── xtrim-api
        │   └── 7.2.0000.0054
        │       ├── xtrim-api-7.2.0000.0054.jar
        │       └── xtrim-api-7.2.0000.0054.pom
        └── xtrim-server
            └── 7.2.0000.0054
                ├── xtrim-server-7.2.0000.0054.jar
                └── xtrim-server-7.2.0000.0054.pom
```

Next step is to copy this to your local Maven repository. For example:

```
cp -r /tmp/output-dir ~/.m2/repository
```

Then you can simply include DFC in your pom.xml like this:

```
        <dependency>
            <groupId>com.documentum</groupId>
            <artifactId>dfc</artifactId>
            <version>7.2.0000.0054</version>
        </dependency>
```
