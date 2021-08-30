import cv2

upscale = cv2.dnn_superres.DnnSuperResImpl_create()
upscale.readModel("/Users/aditya/Programming/PressureTumorAI/pressuretumorai/model/EDSR_x4.pb")
upscale.setModel("edsr", 4)
# EDSR, ESPCN, FSRCNN, or LapSRN


img = cv2.imread("/Users/aditya/Programming/PressureTumorAI/picture.jpg")
result = upscale.upsample(img)
while True:
    cv2.imshow("Image", result)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
