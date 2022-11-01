dict={
    "js":"Javascript 101",
    "python":["Django","Git"],
    "html":"HTML 101"
}


# Here None is the default value(that is if the key is not present in the dict then that value will taken as None) and css is the key to be found in the dict
if (dict.get("css",None)):
    print("True")
else:
    print("False")    