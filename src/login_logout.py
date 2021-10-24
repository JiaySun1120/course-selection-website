# -*- coding: utf-8 -*-

# --------------------------------------------------------------
#    Description：
#
#
# --------------------------------------------------------------
from flask import session, render_template, Blueprint, request, redirect, url_for, flash
import mysql.connector
import traceback
from config import *

log_bp = Blueprint('log', __name__)


@log_bp.route('/logout', methods=['GET'])
def logout():
    session.clear()  # 清空session
    return redirect(url_for('home'))


@log_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mydb = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            passwd=mysql_passwd,
            db=mysql_db)

        print(mydb)
        cur = mydb.cursor()

        # print(request.form['role'])

    # 管理员登录
        if request.form['role'] == 'Admin':
            sql = "select AdminPassword,AdminName from AdminInfo where AdminNo=%s" % (
                request.form['username'])
            try:
                cur.execute(sql)
                cur_res = cur.fetchall()
                if cur_res != []:
                    if cur_res[0][0] != request.form['password']:

                        flash(u'wrong password', 'warning')
                        return render_template('login.html')
                    else:
                        session['No'] = request.form['username']
                        session['name'] = cur_res[0][1]
                        session['logged_in'] = True
                        session['identity'] = 'admin'
                        session['password'] = request.form['password']
                        return redirect(url_for('admin.admin_index'))
            except Exception as e:
                print(traceback.print_exc())

    # 教师登录
        elif request.form['role'] == 'Teacher':
            sql = "select TeacherPassword,TeacherName,TeaCollegeNo from TeacherInfo where TeacherNo=%s" % (
                request.form['username'])
            try:
                cur.execute(sql)
                cur_res = cur.fetchall()
                if cur_res != []:
                    # if cur_res[0][0] != request.form['password']:
                    if cur_res[0][0] != request.form['password']:
                        flash(u'wrong password', 'warning')
                        return render_template('login.html')
                    else:
                        session['No'] = request.form['username']
                        session['name'] = cur_res[0][1]
                        session['logged_in'] = True
                        session['identity'] = 'teacher'
                        session['password'] = request.form['password']
                        session['college'] = cur_res[0][2]
                        
                        cur.execute("select CollegeName from CollegeInfo where CollegeNo=%s" % (
                            session['college']))
                        session['collegeName'] = cur.fetchall()[0][0]
                        print(session)
                        return redirect(url_for('teacher.teacher_index'))
            except Exception as e:
                print(traceback.print_exc())

    # 学生登录
        elif request.form['role'] == 'Student':
            sql = "select StudentPassword,StudentName,CollegeNo,SpecialityNo,StudentGender,StudentBirthday from StudentInfo where StudentNo=%s" % (
                request.form['username'])
            try:
                cur.execute(sql)
                cur_res = cur.fetchall()
                if cur_res != []:
                    # if cur_res[0][0] != request.form['password']:
                    if cur_res[0][0] != request.form['password']:
                        flash(u'wrong password', 'warning')
                        return render_template('login.html')
                    else:
                        session['No'] = request.form['username']
                        session['name'] = cur_res[0][1]
                        session['logged_in'] = True
                        session['identity'] = 'student'
                        session['password'] = request.form['password']
                        session['college'] = cur_res[0][2]
                        session['speciality'] = cur_res[0][3]
                        session['gender'] = cur_res[0][4]
                        session['birthday'] = cur_res[0][5]

                        cur.execute("select SpecialityName from SpecialityInfo where SpecialityNo=%s" % (
                            session['speciality']))
                        session['specialityName'] = cur.fetchall()[0][0]

                        cur.execute("select CollegeName from CollegeInfo where CollegeNo=%s" % (
                            session['college']))
                        session['collegeName'] = cur.fetchall()[0][0]
                        print(session)
                        return redirect(url_for('student.student_index'))
            except Exception as e:
                print(traceback.print_exc())

        flash(u'You have chosen the role {}, please check your username and password!'.format(
            request.form['role']), 'warning')
    return render_template('login.html')
