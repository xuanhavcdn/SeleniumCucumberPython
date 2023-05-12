class TestUpload:
    # define locators
    URL = "https://demo.guru99.com/test/upload/"
    UploadFileBtn = "//input[@id='uploadfile_0']"
    SubmitBtn = "//button[@id='submitbutton']"
    SuccessMessageCss = "h3[style='color: rgb(255, 255, 255); display: block;']"
    ErrorMessageCss = "h3[style='color: rgb(255, 255, 255); display: block;']"
    CheckBoxTermOfService = "//input[@id='terms']"
    TermOfServiceURL = "//a[normalize-space()='terms of service']"
    TermOfServicePage = "https://demo.guru99.com/test/upload/rules.php"
    fileUploadURL = "/Users/ha.cao/Desktop/Clone/FileTest/"
