import cv2
import os

def center_crop(img, dim):
  """Returns center cropped image

  Args:
  img: image to be center cropped
  dim: dimensions (width, height) to be cropped from center
  """
  width, height = img.shape[1], img.shape[0]
  #process crop width and height for max available dimension
  crop_width = dim[0] if dim[0]<img.shape[1] else img.shape[1]
  crop_height = dim[1] if dim[1]<img.shape[0] else img.shape[0]
  mid_x, mid_y = int(width/2), int(height/2)
  cw2, ch2 = int(crop_width/2), int(crop_height/2)
  crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
  return crop_img

def scale_image(img, factor=1):
  """Returns resize image by scale factor.
  This helps to retain resolution ratio while resizing.
  Args:
  img: image to be scaled
  factor: scale factor to resize
  """
  return cv2.resize(img, (int(img.shape[1] * factor), int(img.shape[0] * factor)))


directory = "../../results/australia/image"
dims = (1400, 1000)
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
      image = cv2.imread(f)
      width, height = image.shape[1], image.shape[0]
      if not(width > dims[0] and height > dims[1]):
        factor = max(dims[0] / width, dims[1] / height)
        image = scale_image(image, factor=factor)
      res = center_crop(image, dims)
      cv2.imwrite("output/" + filename, res)