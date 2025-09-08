# This function checks visibility / if the ISS is in the sun or not
def checkVisibility(visibility): 
    if visibility == "shadow":
        print("The ISS is in the shadow of the Earth.")
    else:
        print("The ISS is in daylight!")
    
# defines the latitude and the visibility
latitude = 51.68  
visibility = "shadow"

#main loop
for i in range(3):
    if latitude > 0:
        print("Hello from the northern hemisphere!")
    else:
        print("Hello from the southern hemisphere!")
    
    checkVisibility(visibility)
