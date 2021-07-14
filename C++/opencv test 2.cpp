#include <opencv2/opencv.hpp>
#include <iostream>
#include <opencv2\imgproc\types_c.h>

using namespace std;
using namespace cv;


int main()
{
	Mat srcImage = imread("C:\\Users\\zhouyidong\\Lena.jpeg");
	if (!srcImage.data)
	{
		cout << "读入图片错误！" << endl;
		return -1;
	}
	imshow("原始图", srcImage);
	//创建输出矩阵
	Mat dstImage(srcImage.size(), srcImage.type());
	//定义x和y方向的矩阵
	Mat xMap(srcImage.size(), CV_32FC1);
	Mat yMap(srcImage.size(), CV_32FC1);
	//获取图像的宽和高
	int rowNumber = srcImage.rows;
	int colNumber = srcImage.cols;

	//对图像进行遍历操作
	for (int i = 0; i < rowNumber; i++)
	{
		for (int j = 0; j < colNumber; j++)
		{
			//x和y都进行翻转操作
			xMap.at<float>(i, j) = static_cast<float>(srcImage.cols - j);
			yMap.at<float>(i, j) = static_cast<float>(srcImage.rows - i);
		}
	}

	//进行重映射操作
	remap(srcImage, dstImage, xMap, yMap,
		CV_INTER_LINEAR, BORDER_CONSTANT, Scalar(0, 0, 0));
	imshow("映射效果图", dstImage);
	waitKey();
	return 0;
}
