import SimpleITK as sitk

def dicom2png(dimage):
    img = sitk.ReadImage(dimage)
    # rescale intensity range from [-1000,1000] to [0,255]
    img = sitk.IntensityWindowing(img, -1000, 1000, 0, 255)
    # convert 16-bit pixels to 8-bit
    img = sitk.Cast(img, sitk.sitkUInt8)

    sitk.WriteImage(img, "new3.png")
    return img

dicom2png('C:\\Users\\Chiraag\\Desktop\\test_lab\\CT_small.dcm')
