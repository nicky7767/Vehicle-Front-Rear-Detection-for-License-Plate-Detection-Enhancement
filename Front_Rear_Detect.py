
from os.path import splitext, basename, join

import numpy as np
import cv2
import traceback

from src.draw_BB import draw_bb
from WPOD_src.label import Label
from WPOD_src.utils import image_files_from_folder

import darknet.python.darknet as dn
import time
# best:FRNet_YOLOv3_50000.weights
FR_weights = b'data/FRD/FRNet_YOLOv3_50000.weights'
FR_netcfg = b'data/FRD/FRNet_YOLOv3.cfg'
FR_data = b'data/FRD/FRNet_YOLOv3.data'


print('FRD Net pre-loading...')
FR_net = dn.load_net(FR_netcfg, FR_weights, 0)
FR_meta = dn.load_meta(FR_data)
threshold = 0.5


def fr_detect(img):
	print('\t\t\tdetecting front and rear using FRD..., Model:', FR_netcfg)
	results, wh = dn.detect(FR_net, FR_meta, img, threshold)

	# the results will be list according to its probability , high prob -> low prob
	if len(results):
		print('\t\t\tFR detection completed')
		FRs = []
		category = []
		for i, result in enumerate(results):
			WH = np.array(img.shape[1::-1], dtype=float)
			cx, cy, w, h = (np.array(result[2]) / np.concatenate((WH, WH))).tolist()
			tl = np.array([cx - w / 2., cy - h / 2.])
			br = np.array([cx + w / 2., cy + h / 2.])
			print('\t\t\tFR number', i, 'position:', tl, br, 'prob:', result[1])
			FRs.append(Label(tl=tl, br=br))
			category.append(result[0])
		return np.array(FRs), category

	else:
		print('\t\t\tFR detection failed')


if __name__ == '__main__':
	input_dir = 'samples/kr'
	output_dir = 'output'
	# imgs_paths = image_files_from_folder(input_dir)
	imgs_paths = ['samples/test_samples/Screenshot from 2022-06-08 21-32-53.png']
	imgs_paths.sort()
	start_time = time.time()
	for img_path in imgs_paths:
		img = cv2.imread(img_path)
		bname = basename(splitext(img_path)[0])

		try:
			FRs, cate = fr_detect(img)

			for i in range(len(FRs)):
				draw_bb(img, FRs[i], cate=cate[i].decode('UTF-8'))
			print("--- %s seconds ---" % (time.time() - start_time))
		except:
			traceback.print_exc()
		cv2.imwrite(join(output_dir, bname + '_out.jpg'), img)
