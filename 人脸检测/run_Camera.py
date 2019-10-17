# -*- coding: utf-8 -*-

# 思绪无限
# 博客网址：https://wuxian.blog.csdn.net/
# Created by: PyQt5 UI code generator 5.11.3
# 运行程序需安装：pyqt5、OpenCV-python


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import time
import cv2
import dlib
import numpy as np
import sys
class Ui_detection(object):
    def __init__(self, MainWindow):

        self.timer_camera = QtCore.QTimer() # 定时器
        self.setupUi(MainWindow)
        self.retranslateUi(MainWindow)
        self.cap = cv2.VideoCapture() # 内置摄像头，可以读取视频
        self.CAM_NUM = 0
        self.face_cascade = cv2.CascadeClassifier('haarcascade_files/haarcascade_frontalface_default.xml')
        self.slot_init() # 设置槽函数
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('G:\\shape_predictor_68_face_landmarks.dat')



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(765, 645)
        MainWindow.setMinimumSize(QtCore.QSize(765, 645))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/pic/pai.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(9800, 9800))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 15, -1, 30)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open.setEnabled(True)
        self.pushButton_open.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_open.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(12)
        self.pushButton_open.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/pic/g1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_open.setIcon(icon1)
        self.pushButton_open.setObjectName("pushButton_open")
        self.horizontalLayout.addWidget(self.pushButton_open)
        self.pushButton_take = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_take.sizePolicy().hasHeightForWidth())
        self.pushButton_take.setSizePolicy(sizePolicy)
        self.pushButton_take.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_take.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(12)
        self.pushButton_take.setFont(font)
        self.pushButton_take.setIcon(icon)
        self.pushButton_take.setObjectName("pushButton_take")
        self.horizontalLayout.addWidget(self.pushButton_take)
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_close.setMaximumSize(QtCore.QSize(130, 40))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(12)
        self.pushButton_close.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/pic/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon2)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_face = QtWidgets.QLabel(self.centralwidget)
        self.label_face.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_face.sizePolicy().hasHeightForWidth())
        self.label_face.setSizePolicy(sizePolicy)
        self.label_face.setMinimumSize(QtCore.QSize(0, 0))
        self.label_face.setMaximumSize(QtCore.QSize(9800, 9800))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_face.setFont(font)
        self.label_face.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_face.setStyleSheet("background-color: rgb(192, 218, 255);")
        self.label_face.setAlignment(QtCore.Qt.AlignCenter)
        self.label_face.setObjectName("label_face")
        self.verticalLayout.addWidget(self.label_face)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionGoogle_Translate = QtWidgets.QAction(MainWindow)
        self.actionGoogle_Translate.setObjectName("actionGoogle_Translate")
        self.actionHTML_type = QtWidgets.QAction(MainWindow)
        self.actionHTML_type.setObjectName("actionHTML_type")
        self.actionsoftware_version = QtWidgets.QAction(MainWindow)
        self.actionsoftware_version.setObjectName("actionsoftware_version")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸实时检测-camera"))
        self.label.setText(_translate("MainWindow", "人脸实时检测"))
        self.pushButton_open.setToolTip(_translate("MainWindow", "点击打开摄像头"))
        self.pushButton_open.setText(_translate("MainWindow", "打开摄像头"))
        self.pushButton_take.setToolTip(_translate("MainWindow", "点击拍照"))
        self.pushButton_take.setText(_translate("MainWindow", "拍照"))
        self.pushButton_close.setToolTip(_translate("MainWindow", "点击关闭摄像头"))
        self.pushButton_close.setText(_translate("MainWindow", "关闭摄像头"))
        self.label_face.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/newPrefix/pic/Hint.png\"/><span style=\" font-size:25pt;\">点击摄像头，实时检测人脸</span><br/></p></body></html>"))


    def slot_init(self):
        # 设置槽函数
        self.pushButton_open.clicked.connect(self.button_open_camera_click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.pushButton_close.clicked.connect(self.closeEvent)
        self.pushButton_take.clicked.connect(self.takePhoto)

    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(
                    self, u"Warning", u"请检测相机与电脑是否连接正确",
                    buttons=QtWidgets.QMessageBox.Ok,
                    defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)

    def show_camera(self):
        flag, self.image = self.cap.read()

        self.image = cv2.flip(self.image, 1)  # 左右翻转

        img_gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        faces = self.detector(img_gray, 0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        for i in range(len(faces)):
            # 取特征点坐标
            landmarks = np.matrix([[p.x, p.y] for p in self.predictor(self.image, faces[i]).parts()])
            for idx, point in enumerate(landmarks):
                # 68 点的坐标
                pos = (point[0, 0], point[0, 1])

                # 利用 cv2.circle 给每个特征点画一个圈，共 68 个
                cv2.circle(self.image, pos, 2, color=(255, 255, 255))
                # 利用 cv2.putText 写数字 1-68
                cv2.putText(self.image,'*', pos, font, 0.2,(255, 255, 255), 1, cv2.LINE_AA)

        show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # 左右翻转
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_face.setPixmap(QtGui.QPixmap.fromImage(showImage))
        self.label_face.setScaledContents(True)

    def takePhoto(self):
        if self.timer_camera.isActive() != False:
            now_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
            print(now_time)
            cv2.imwrite('pic_' + str(now_time) + '.png', self.image)


            self.timer_camera.stop()  # 停止计时
            # gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            # faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            # for (x, y, w, h) in faces:
            #     cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 255, 0), 2)
                # 取特征点坐标
            img_gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
            faces = self.detector(img_gray, 0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            for i in range(len(faces)):
                # 取特征点坐标
                landmarks = np.matrix([[p.x, p.y] for p in self.predictor(self.image, faces[i]).parts()])
                for idx, point in enumerate(landmarks):
                    # 68 点的坐标
                    pos = (point[0, 0], point[0, 1])

                    # 利用 cv2.circle 给每个特征点画一个圈，共 68 个
                    cv2.circle(self.image, pos, 2, color=(255, 255, 255))
                    # 利用 cv2.putText 写数字 1-68
                    cv2.putText(self.image,'*', pos, font, 0.2,(255, 255, 255), 1, cv2.LINE_AA)


            show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # 左右翻转
            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
            self.label_face.setPixmap(QtGui.QPixmap.fromImage(showImage))
            self.label_face.setScaledContents(True)



    def closeEvent(self):
        if self.timer_camera.isActive() != False:
            ok = QtWidgets.QPushButton()
            cacel = QtWidgets.QPushButton()

            msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"关闭", u"是否关闭！")

            msg.addButton(ok,QtWidgets.QMessageBox.ActionRole)
            msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
            ok.setText(u'确定')
            cacel.setText(u'取消')

            if msg.exec_() != QtWidgets.QMessageBox.RejectRole:

                if self.cap.isOpened():
                    self.cap.release()
                if self.timer_camera.isActive():
                    self.timer_camera.stop()
                self.label_face.setText("<html><head/><body><p align=\"center\"><img src=\":/newPrefix/pic/Hint.png\"/><span style=\" font-size:26pt;\">点击摄像头，实时检测人脸</span><br/></p></body></html>")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_detection(window)
    window.show()
    sys.exit(app.exec_())

