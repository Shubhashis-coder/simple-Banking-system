#Admin
from tkinter import *
from tkinter import messagebox
import os,datetime,random,shutil

class transact(object):
    def __init__(self):
        self.transaction()
    def transaction(self):        
        def deposit_():            
            def deposit_entry():
                fh=open('tot_userid.txt','r+')
                if '$'+str(trans_acc.get())+'$' in fh.read():
                    fh.seek(0)
                    for x in  fh.readlines():
                        splt=x.split('$')
                        if splt[1]==str(trans_acc.get()):
                            user_id=(splt[2])
                else:
                    messagebox.showerror('Error','This Account no is not in our database ,Please check it')
                    return                 
                fh_=open('cust_data/'+user_id+'/transaction.txt','r+')
                money=fh_.readlines()[-1]
                st=money.split('$')
                money=st[2]
                file=open('cust_data/'+user_id+'/transaction.txt','a+')
                amount=e1.get()
                if int(e1.get())<=0:
                    messagebox.showerror('Error','Amount Not valid')
                    return
                else:
                    pass
                new_money=str(int(money)+int(amount))               
                file.writelines(['$'+str(datetime.datetime.now().day)+'/'+str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().year)+'$'+new_money+'$'+amount+'$'+'Deposit'+'$'+'\n'])
                def transaction_successful():
                    messagebox.showinfo('Succcess','Transaction Successful')
                    deposit.destroy()
                transaction_successful()         
            fh=open('tot_userid.txt','r+')
            if '$'+str(trans_acc.get())+'$' in fh.read():
                fh.seek(0)
                for x in  fh.readlines():
                    splt=x.split('$')
                    if splt[1]==str(trans_acc.get()):
                        user_id=(splt[2])
            else:
                messagebox.showerror('Error','This Account no is not in our database ,Please check it')
                return                 
            fh_=open('cust_data/'+user_id+'/transaction.txt','r+')
            money=fh_.readlines()[-1]
            st=money.split('$')
            money=st[2]
            deposit=Tk()         
            deposit.iconbitmap('bank.ico')
            deposit.config(bg='#D6F5FF')
            Label(deposit, text='Available Amount:-  '+money, width=22, anchor='center',font=('Arial',16),bg='#D6F5FF' ).pack(padx=10,pady=10)
            deposit.title('Enter Deposit Amount')
            e1=Entry(deposit,bd=5)
            e1.pack()        
            button=Button(deposit,text='Continue',command=deposit_entry)
            button.pack(pady=10)
        def withdrawl_():
            def withdrawl_entry():
                fh=open('tot_userid.txt','r+')
                if '$'+str(trans_acc.get())+'$' in fh.read():
                    fh.seek(0)
                    for x in  fh.readlines():
                        splt=x.split('$')
                        if splt[1]==str(trans_acc.get()):
                            user_id=(splt[2])
                else:
                    messagebox.showerror('Error','This Account no is not in our database ,Please check it')
                    return                 
                fh_=open('cust_data/'+user_id+'/transaction.txt','r+')
                money=fh_.readlines()[-1]
                st=money.split('$')
                money=st[2]
                file=open('cust_data/'+user_id+'/transaction.txt','a+')
                amount=e2.get()              
                new_money=str(int(money)-int(amount))
                if int(e2.get())<=0:
                    messagebox.showerror('Error','Amount Not valid')
                    return
                elif int(e2.get())<500:
                    messagebox.showerror('Error','Amount should be more than Rs 500')
                    return
                elif int(e2.get())>int(money):
                    messagebox.showerror('Error','Withdrawl amount exceed current Balance')
                    return
                elif int(new_money)<500:
                    messagebox.showerror('Error','You cannot withdraw this much amount')
                    return
                else:
                    pass
                file.writelines(['$'+str(datetime.datetime.now().day)+'/'+str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().year)+'$'+new_money+'$'+amount+'$'+'Withdrawl'+'$'+'\n'])  
                def transaction_successful():                
                    messagebox.showinfo('Succcess','Transaction Successful')
                    withdrawl.destroy()
                transaction_successful()
            fh=open('tot_userid.txt','r+')
            if '$'+str(trans_acc.get())+'$' in fh.read():
                fh.seek(0)
                for x in  fh.readlines():
                    splt=x.split('$')
                    if splt[1]==str(trans_acc.get()):
                        user_id=(splt[2])
            else:
                messagebox.showerror('Error','This Account no is not in our database ,Please check it')
                return                 
            fh_=open('cust_data/'+user_id+'/transaction.txt','r+')
            money=fh_.readlines()[-1]
            st=money.split('$')
            money=st[2]
            withdrawl=Tk()
            withdrawl.config(bg='#D6F5FF')
            withdrawl.iconbitmap('bank.ico')
            Label(withdrawl, text='Available Amount:-  '+money, width=22, anchor='center',font=('Arial',16),bg='#D6F5FF' ).pack(padx=10,pady=10)
            withdrawl.title('Enter Withdraw Amount')
            e2=Entry(withdrawl,bd=5)
            e2.pack()        
            button=Button(withdrawl,text='Continue',command=withdrawl_entry)
            button.pack(pady=10)  
        self.transact=Tk()
        self.transact.geometry('295x242')
        self.transact.maxsize(height=242,width=295)
        self.transact.iconbitmap('bank.ico')
        self.transact.config(bg='#D6F5FF')
        self.transact.title('Transaction')
        Label(self.transact, text='Enter  Account Number', width=22, anchor='center',font=('Arial',16),bg='#D6F5FF' ).pack(padx=10,pady=10)
        trans_acc=Entry(self.transact,bd=5)
        trans_acc.pack()
        def temp_disp():
            fh=open('tot_userid.txt','r+')
            if '$'+str(trans_acc.get())+'$' in fh.read():
                fh.seek(0)
                for x in  fh.readlines():
                    splt=x.split('$')
                    if splt[1]==str(trans_acc.get()):
                        user_id=(splt[2])
            else:
                messagebox.showerror('Error','This Account no is not in our database ,Please check it')
                return
            fh_=open('cust_data/'+user_id+'/transaction.txt','r+')
            money=fh_.readlines()[-1]
            st=money.split('$')
            money=st[2]
            Label(self.transact,text='Current Balance: '+money, width=22, anchor='center',font=('Times New Roman',14),bg='#D6F5FF' ).pack(padx=10,pady=10)     
            Depo=Button(self.transact,text='Deposit ',command=deposit_)
            Depo.pack()
            Depo.place(x=60,y=170)
            With=Button(self.transact,text='Withdraw',command=withdrawl_)
            With.pack()
            With.place(x=160,y=170)
        Button(self.transact,text='Submit',command=temp_disp).pack(padx=10,pady=10)

class after_sign_in_customer():    
    def __init__(self,userid):
        self.sign_in_after(userid)
        self.userid=userid
    def sign_in_after(self,userid):
        self.sign_in=Tk()
        self.sign_in.geometry('566x227')
        self.sign_in.maxsize(height=227,width=566)
        self.sign_in.title('Account')
        self.sign_in.iconbitmap('bank.ico')
        self.sign_in.config(bg='#D6F5FF')
        def sign_out():
            messagebox.showinfo('Have A Nice Day','You Are Signed Out')
            self.sign_in.destroy()
            start=homepage()
        signout=Button(self.sign_in,anchor='ne',text='Sign Out',command=sign_out)
        signout.pack(side='right')
        signout.place(x=620,y=5)
        def back_sign_in():
            self.acc_info.destroy()
            start=self.sign_in_after(userid)
        def acc_info():
            self.sign_in.destroy()
            self.acc_info=Tk()
            self.acc_info.config(bg="#D6F5FF")
            self.acc_info.iconbitmap('bank.ico')
            self.acc_info.title('Account Database')
            self.acc_info.geometry('298x277')
            file=open('cust_data/'+userid+'/acc_info.txt','r+')
            st=file.readlines()
            acc_label=Label(self.acc_info, text='Account Information',bg="#D6F5FF",font=('PRIMETIME',16), anchor='center')
            acc_label.pack(pady=15)
            name_label=Label(self.acc_info, text='Name',bg="#D6F5FF")
            name_label.pack()
            name_label.place(x=50,y=90)
            name_label1=Label(self.acc_info,text=str(st[0].rstrip('\n')+' '+st[1].rstrip('\n')),bg="#D6F5FF")
            name_label1.pack()
            name_label1.place(x=150,y=90)
            fname_label=Label(self.acc_info,text="Father's Name",bg="#D6F5FF")
            fname_label.pack()
            fname_label.place(x=50,y=115)
            fname_label1=Label(self.acc_info,text=str(st[2]),bg="#D6F5FF")
            fname_label1.pack()
            fname_label1.place(x=150,y=115)
            pan_label=Label(self.acc_info,text="PAN No.",bg="#D6F5FF")
            pan_label.pack()
            pan_label.place(x=50,y=140)
            pan_label1=Label(self.acc_info,text=str(st[4]),bg="#D6F5FF")
            pan_label1.pack()
            pan_label1.place(x=150,y=140)
            mob_no=Label(self.acc_info,text="Mobile No.",bg="#D6F5FF")
            mob_no.pack()
            mob_no.place(x=50,y=165)
            mob_no1=Label(self.acc_info,text=str(st[12]),bg="#D6F5FF")
            mob_no1.pack()
            mob_no1.place(x=150,y=165)
            email_id=Label(self.acc_info,text="Email Id ",bg="#D6F5FF")
            email_id.pack()
            email_id.place(x=50,y=190)
            email_id1=Label(self.acc_info,text=str(st[13]),bg="#D6F5FF")
            email_id1.pack()
            email_id1.place(x=150,y=190)
            Button(self.acc_info,text='Back', anchor='center',command=back_sign_in).pack(side='bottom',padx=10,pady=10)
            self.acc_info.mainloop() 
        def last_5():
            self.sign_in.destroy()
            self.last_5=Tk()
            self.last_5.title('History')
            self.last_5.geometry('390x295')
            self.last_5.maxsize(height=295,width=390)
            self.last_5.config(bg="#D6F5FF")
            self.last_5.iconbitmap('bank.ico')
            self.last_5.title('Account Database')
            def close():
                self.last_5.destroy()
            close_but=Button(self.last_5,text='Close',command=close,anchor='center')
            close_but.pack(side='right')
            close_but.place(x=340,y=10)
            main=Label(self.last_5, text='Last 5 Transactions', anchor='center',font=('Bernard MT Condensed',16),bg="#D6F5FF",padx=15,pady=15 )
            main.pack()
            file=open('cust_data/'+userid+'/transaction.txt','r+')
            fh=file.readlines()
            bal=fh[-1]
            bal=bal.split('$')
            bal=bal[2]
            current_bal=Label(self.last_5, text='Current Balance:- '+bal+'.00', anchor='center',bg="#D6F5FF")
            current_bal.pack()
            current_bal.place(y=60,x=110)
            date=Label(self.last_5, text='Date',bg="#D6F5FF")
            date.pack()
            date.place(x=55,y=100)
            total_bal=Label(self.last_5, text='Current Balance',bg="#D6F5FF")
            total_bal.pack()
            total_bal.place(x=140,y=100)
            status=Label(self.last_5, text='Status',bg="#D6F5FF")
            status.pack()
            status.place(x=260,y=100)
            try:
                data1=fh[-1]
                data1=data1.split('$')
                data1_label1=Label(self.last_5, text=data1[1],bg="#D6F5FF")
                data1_label1.pack()
                data1_label1.place(x=50,y=130)
                data1_label2=Label(self.last_5, text=data1[2],bg="#D6F5FF")
                data1_label2.pack()
                data1_label2.place(x=150,y=130)
                data1_label3=Label(self.last_5, text=data1[3]+'  '+data1[4],bg="#D6F5FF")
                data1_label3.pack()
                data1_label3.place(x=250,y=130)
                data2=fh[-2]
                data2=data2.split('$')
                data2_label1=Label(self.last_5, text=data2[1],bg="#D6F5FF")
                data2_label1.pack()
                data2_label1.place(x=50,y=155)
                data2_label2=Label(self.last_5, text=data2[2],bg="#D6F5FF")
                data2_label2.pack()
                data2_label2.place(x=150,y=155)
                data2_label3=Label(self.last_5, text=data2[3]+'  '+data2[4],bg="#D6F5FF")
                data2_label3.pack()
                data2_label3.place(x=250,y=155)
                data3=fh[-3]
                data3=data3.split('$')
                data3_label1=Label(self.last_5, text=data3[1],bg="#D6F5FF")
                data3_label1.pack()
                data3_label1.place(x=50,y=180)
                data3_label2=Label(self.last_5, text=data3[2],bg="#D6F5FF")
                data3_label2.pack()
                data3_label2.place(x=150,y=180)
                data3_label3=Label(self.last_5, text=data3[3]+' '+data3[4],bg="#D6F5FF")
                data3_label3.pack()
                data3_label3.place(x=250,y=180)
                data4=fh[-4]
                data4=data4.split('$')
                data4_label1=Label(self.last_5, text=data4[1],bg="#D6F5FF")
                data4_label1.pack()
                data4_label1.place(x=50,y=205)
                data4_label2=Label(self.last_5, text=data4[2],bg="#D6F5FF")
                data4_label2.pack()
                data4_label2.place(x=150,y=205)
                data4_label3=Label(self.last_5, text=data4[3]+' '+data4[4],bg="#D6F5FF")
                data4_label3.pack()
                data4_label3.place(x=250,y=205)
                data5=fh[-5]
                data5=data5.split('$')
                data5_label1=Label(self.last_5, text=data5[1],bg="#D6F5FF")
                data5_label1.pack()
                data5_label1.place(x=50,y=230)
                data5_label2=Label(self.last_5, text=data5[2],bg="#D6F5FF")
                data5_label2.pack()
                data5_label2.place(x=150,y=230)
                data5_label3=Label(self.last_5, text=data5[3]+' '+data5[4],bg="#D6F5FF")
                data5_label3.pack()
                data5_label3.place(x=250,y=230)
            except IndexError:
                pass            
        def total_balance():
            fh=open('cust_data/'+userid+'/transaction.txt','r+')
            file=fh.readlines()
            file=file[-1]
            file=file.split('$')
            file=file[2]
            messagebox.showinfo('Balance','Total Balance in your account is '+file+'.')
            return
        cm=Label(self.sign_in, text='Welcome to Account Management System', anchor='center',font=('Pricedown Bl',18),bg='#D6F5FF' )
        cm.pack()                 
        cm.place(x=67,y=40)
        choose=Label(self.sign_in, text='Choose The Required Option', anchor='w',padx=15,pady=15 ,font=('Pricedown Bl',16),bg='#D6F5FF')
        choose.pack()
        choose.place(x=140,y=70)
        info=Button(self.sign_in,text='Account Information',command=acc_info)
        info.pack()
        info.place(x=90,y=130)
        last_5=Button(self.sign_in,text='Last 5 Transaction',command=last_5)
        last_5.pack()
        last_5.place(x=230,y=130)
        total_bal=Button(self.sign_in,text='View Total Balance',command=total_balance)
        total_bal.place(x=350,y=130)
        self.sign_in.mainloop()         

class account(object):
    def __init__(self):
        self.sign_in()
    def retrive_home(self):
        self.window.destroy()
        start=home_page()       
    def sign_in(self):
        self.window=Tk()
        self.window.geometry('350x220')
        self.window.maxsize(height=220,width=350)
        self.window.config(bg="#D6F5FF")
        self.window.iconbitmap('bank.ico')
        self.window.title('Admin Login')
        def admin_check():
            if self.entry_check1.get()=='' or self.entry_check2.get()=='':
                messagebox.showerror('Error','Blank Username or Password')
                return            
            if self.entry_check1.get()=="Admin" and self.entry_check2.get()=="000000":
                messagebox.showinfo('Welcome to Database','Welcome  Admin')    
                self.window.destroy()
                start=admin_win()
            else:
                messagebox.showerror('Error','Invalid Login Please Check credentials')        
        user_id=Label(self.window,text='Enter Your User Id',bg="#D6F5FF")
        user_id.pack(padx=15,pady=5,anchor='center')
        self.entry_check1=Entry(self.window,bd=5)
        self.entry_check1.pack(padx=15,pady=5,anchor='center')
        pwd=Label(self.window,text='Enter Your Password',bg="#D6F5FF")
        pwd.pack(padx=15,pady=5,anchor='center')
        self.entry_check2=Entry(self.window,bd=5,show='+')
        self.entry_check2.pack(padx=15,pady=5,anchor='center')
        button=Button(self.window,text='Sign In',command=admin_check)
        button.pack(padx=5,side=RIGHT)
        button1=Button(self.window,text='Cancel',command=self.retrive_home)
        button1.pack(padx=5,side=LEFT)
        self.window.mainloop()

def admin_win():
    admin_win2=Tk()
    admin_win2.title('Admin')
    admin_win2.geometry('354x155')
    admin_win2.config(bg="#D6F5FF")
    admin_win2.iconbitmap('bank.ico')
    def delete_account():
        del_account=Tk()
        del_account.iconbitmap('bank.ico')
        del_account.title('Delete Account')
        del_account.config(bg="#D6F5FF")
        del_account.geometry('277x140')
        del_account.maxsize(height=140,width=277)
        def delete(): 
            acc_no=Enter_acc_no.get()
            if acc_no=='':
                messagebox.showerror('Error','Blank  Account Number')
                return
            fh=open('tot_userid.txt','r+')
            if '$'+str(acc_no)+'$' in fh.read():
                fh.seek(0)
                for x in  fh.readlines():
                    splt=x.split('$')
                    if splt[1]==str(acc_no):
                        user_id=splt[2]
            else:
                messagebox.showerror('Error','Incorrect Account No. \nPlease Try Again')
                return 
            dir='cust_data/'+user_id
            try:
                shutil.rmtree(dir)
                fh=open('tot_userid.txt','r+')
                fh1=open('new.txt','a+')   
            except OSError as e:
                print ("Error: %s - %s." % (e.filename, e.strerror))
            del_account.destroy()
            final=Tk()
            final.config(bg="#D6F5FF")
            final.geometry('374x90')
            final.maxsize(height=90,width=374)
            final.iconbitmap('bank.ico')
            final.title('Succesful')
            Label(final, text='Account Sucessfully Deleted', anchor='center',font=('PRIMETIME',15)).pack(padx=15,pady=15)
            Button(final,text='Close',command=lambda:final.destroy()).pack()
        Label(del_account, text='Account Number', anchor='center',font=('PRIMETIME',15),bg="#D6F5FF").pack(padx=10,pady=10)
        Enter_acc_no=Entry(del_account)
        Enter_acc_no.pack(padx=5,pady=5)
        Button(del_account,text='Submit',command=delete).pack(padx=5,pady=15)
    def New():
        admin_win2.destroy()
        entries=[]
        new=Tk()
        new.title('Enter Details')
        new.config(bg="#D6F5FF")
        new.iconbitmap('bank.ico')       
        fh=open('tot_userid.txt')
        def unq_user(Usrnm):
            f=open("tot_userid.txt","r")
            if "$"+Usrnm+"$" in f.read():
                messagebox.showerror('Error','This User id is already taken, Please try another combination')
                return(False)
            elif Usrnm[0].isdigit():
                messagebox.showerror('Error','Username must not start with a digit.')
                return(False)
            elif not(Usrnm.islower()):
                messagebox.showerror('Error','Username must contain only lowercase letters.')
                return(False)
            elif not(Usrnm.isalnum()):
                messagebox.showerror('Error','Extra characters are not allowed.')
                return(False)
            elif len(Usrnm)<6:
                messagebox.showerror('Error','Username is very small, give a big one.')
                return(False)
            else:
                return(True)
        def check_details():
            MsgBox = messagebox.askquestion ('Save and Continue','Are you sure you want to save and continue to save the application and continue',icon = 'warning')
            if MsgBox == 'yes':
                if e21.get()!='':
                    if unq_user(e21.get())==True:
                        if e1.get()=='' or e2.get()=='' or e3.get()=='' or e4.get()=='' or e7.get()=='' or e10.get()=='' or e11.get()=='' or e12.get()=='' or e13.get()=='' or e14.get()=='':
                            messagebox.showerror('Error','All Fields are Mandatory')
                            return(False)
                        elif e16.get()=='' or e17.get()=='' or e18.get()=='' or e19.get()=='' or e20.get()=='' :
                            messagebox.showerror('Error','All Fields are Mandatory')
                            return(False)
                        elif not(e1.get().isalpha()):
                            messagebox.showerror('Error','Only Alphabets are Allowed. Check First Name')
                            return(False)
                        elif not(e2.get().isalpha()):
                            messagebox.showerror('Error','Only Alphabets are Allowed. Check Last Name')
                            return(False)
                        elif not(e7.get().isalnum()):
                            messagebox.showerror('Error',"No Special Characters Allowed,Check PAN No.")
                            return(False)
                        elif not(e11.get().isalpha()):
                            messagebox.showerror('Error',"Only Alphabets are Allowed,Check City")
                            return(False)
                        elif not(e12.get().isalpha()):
                            messagebox.showerror('Error',"Only Alphabets are Allowed,Check State")
                            return(False)
                        elif not(e13.get().isalnum()):
                            messagebox.showerror('Error',"Only Integers Are Allowed,Check PIN Code")
                            return(False)
                        elif not(e14.get().isalpha()):
                            messagebox.showerror('Error',"Only Alphabets are Allowed,Check Country")
                            return(False)
                        elif not(e16.get().isalpha()):
                            messagebox.showerror('Error',"Only Alphabets are Allowed,Check Nationality")
                            return(False)
                        elif not(e17.get().isalnum()):
                            messagebox.showerror('Error',"Only Integers Are Allowed,Check Mob No.")
                            return(False)
                        elif not(e19.get().isalnum()):
                            messagebox.showerror('Error',"Only Integers Are Allowed,Check Opening Balance")
                            return(False)
                        elif not(e20.get().isalnum()):
                            messagebox.showerror('Error',"Only Integers Are Allowed,Check Monthly Income")
                            return(False)
                        elif int(e19.get())<500:
                            messagebox.showerror('Error',"Opening Blance Should be greater than Rs. 500/-")
                            return(False)
                        else:
                            pass                                              
                        entries=[]
                        entries.append(e1.get()+'\n')
                        entries.append(e2.get()+'\n')
                        entries.append(e3.get()+'\n')
                        entries.append(e4.get()+'\n')
                        entries.append(e6.get()+'\n')
                        entries.append(e7.get()+'\n')
                        entries.append(e10.get()+'\n')
                        entries.append(e11.get()+'\n')
                        entries.append(e12.get()+'\n')
                        entries.append(e13.get()+'\n')
                        entries.append(e14.get()+'\n')
                        entries.append(e16.get()+'\n')
                        entries.append(e17.get()+'\n')
                        entries.append(e18.get()+'\n')
                        entries.append(e19.get()+'\n')
                        st=str(e5.get())
                        for x in entries:
                            if x=="":
                                messagebox.showerror("Error","plese do fill all ")
                                return
                        fh=open('acc_no.txt','r+')
                        acc_new=str(int(fh.readlines()[-1].rstrip('\n'))+1)
                        fh.writelines([acc_new+'\n'])
                        entries.append(acc_new+'\n')                        
                        u=e21.get()
                        fh_=open('tot_userid.txt','a+')
                        fh_.writelines('$'+acc_new+'$'+u+'$'+'\n')
                        pwd=random.randint(100000,9999999)                        
                        dire='cust_data/'+u 
                        os.mkdir(dire)
                        pwd_create=open('cust_data/'+u+'/security.txt','a+')
                        pwd_create.writelines(['$'+u+'$'+str(pwd)+'$'+'\n'])
                        balance=open('cust_data/'+u+'/'+'transaction.txt','a+')
                        balance.writelines(['$'+str(datetime.datetime.now().day)+'/'+str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().year)+'$'+str(e19.get())+'$'+'Opening Balance'+'$'+'\n'])
                        record=open('cust_data/'+u+'/'+'acc_info'+".txt","a+")
                        record.writelines(entries)                                
                        new.destroy()
                        submit=Tk()
                        submit.geometry('307x205')
                        submit.title('Note the following')
                        submit.iconbitmap('bank.ico')
                        submit.config(bg="#D6F5FF")
                        submit.maxsize(height=205,width=307)
                        def retrieve_home():
                            submit.destroy()
                            start=admin_win()
                        ap=Label(submit, text="Application Submitted",bg="#D6F5FF", anchor='center',font=('PRIMETIME',14)).pack(padx=10,pady=10)                        
                        userid=Label(submit, text="User Id:",bg="#D6F5FF")
                        userid.pack()
                        userid.place(x=70,y=60)
                        userid1=Label(submit, text=u,bg="#D6F5FF")
                        userid1.pack()
                        userid1.place(x=190,y=60)
                        pwd2=Label(submit, text="Password: ",bg="#D6F5FF")
                        pwd2.pack()
                        pwd2.place(x=70,y=85)
                        pwd1=Label(submit, text=str(pwd),bg="#D6F5FF")
                        pwd1.pack()
                        pwd1.place(x=190,y=85)
                        acc=Label(submit, text="Account Number:",bg="#D6F5FF")
                        acc.pack()
                        acc.place(x=70,y=115)
                        acc1=Label(submit, text=str(acc_new),bg="#D6F5FF")
                        acc1.pack()
                        acc1.place(x=190,y=115)
                        Button(submit,text='Back',anchor='center',command=retrieve_home).pack(side='bottom',pady=10)

                else:
                    messagebox.showerror("Error","Please Enter the Username")
                    return
            else:
                messagebox.showinfo('Return','You will now return to the application screen')                
        L1=Label(new, text="First Name", width=22, anchor='w',padx=5,pady=5 ,bg="#D6F5FF")
        L1.grid(row=0)
        L2=Label(new, text="Last Name", width=22, anchor='w',padx=5,pady=5,bg="#D6F5FF")
        L2.grid(row=1)
        L3=Label(new, text="Father's Name", width=22, anchor='w',padx=5,pady=5,bg="#D6F5FF" )
        L3.grid(row=2)
        L4=Label(new, text="Mother's Name", width=22, anchor='w',padx=5,pady=5,bg="#D6F5FF")
        L4.grid(row=3)
        L5=Label(new, text="Date of Birth [DD/MM/YYYY]", width=22, anchor='w',padx=5,pady=5,bg="#D6F5FF")
        L5.grid(row=4)
        l1=Label(new,text='Gender',width=22,anchor='w',padx=5,pady=5,bg="#D6F5FF").grid(row=5)
        L6=Label(new, text="PAN No.", width=22, anchor='w',padx=5,pady=5,bg="#D6F5FF")
        L6.grid(row=6)
        l2=Label(new,text='Category',width=22,anchor='w',padx=5,pady=5,bg="#D6F5FF").grid(row=7)
        l2=Label(new,text='Religion',width=22,anchor='w',padx=5,pady=5,bg="#D6F5FF").grid(row=9)
        L7=Label(new, text="Address", width=22, anchor='w',padx=5,pady=5,bg="#D6F5FF")
        L7.grid(row=11)    
        L8=Label(new, text="City", width=22, anchor='w',padx=5,pady=5,bg="#D6F5FF")
        L8.grid(row=12)
        L9=Label(new, text="State", width=22, anchor='w',padx=5,pady=5,bg="#D6F5FF" )
        L9.grid(row=13)
        L10=Label(new, text="PIN Code", width=22, anchor='w',padx=5,pady=5 ,bg="#D6F5FF")
        L10.grid(row=14)
        L11=Label(new, text="Country", width=22, anchor='w',padx=5,pady=5,bg="#D6F5FF")
        L11.grid(row=15)
        L13=Label(new, text="Nationality", width=22, anchor='w',padx=5,pady=5,bg="#D6F5FF")
        L13.grid(row=17)
        L14=Label(new, text="Mob No.", width=22, anchor='w',padx=5,pady=5,bg="#D6F5FF").grid(row=18)
        L15=Label(new, text="Email Id", width=22, anchor='w',padx=5,pady=5,bg="#D6F5FF").grid(row=19)
        L16=Label(new, text="Opening Balance", width=22, anchor='w',padx=5,pady=5 ,bg="#D6F5FF").grid(row=20)
        L17=Label(new, text="Monthly Income", width=22, anchor='w',padx=5,pady=5,bg="#D6F5FF").grid(row=21)
        L18=Label(new, text='\nCreate Your Unique User Id',width=22, anchor='center',padx=5,pady=5,bg="#D6F5FF").grid(row=22,column=0)
        L2=Button(new,text="Continue",anchor='center',command=check_details).grid(row=22,column=2)        
        e1 = Entry(new)
        e2 = Entry(new)
        e3 = Entry(new)
        e4 = Entry(new)
        e5 = Entry(new)
        e6 = Entry(new)
        e7 = Entry(new)        
        e10 = Entry(new)
        e11 = Entry(new)
        e12 = Entry(new)
        e13 = Entry(new)
        e14 = Entry(new)
        e16 = Entry(new)
        e17 = Entry(new)
        e18 = Entry(new)
        e19 = Entry(new)
        e20 = Entry(new)
        e21 = Entry(new)
        e1.grid(row=0, column=1,padx=5,pady=5)
        e2.grid(row=1, column=1,padx=5,pady=5)
        e3.grid(row=2, column=1,padx=5,pady=5)
        e4.grid(row=3, column=1,padx=5,pady=5)
        e5.grid(row=4, column=1,padx=5,pady=5)
        e6.grid(row=5, column=1,padx=5,pady=5)
        e7.grid(row=6, column=1,padx=5,pady=5)
        e10.grid(row=11, column=1,padx=5,pady=5)
        e11.grid(row=12, column=1,padx=5,pady=5)
        e12.grid(row=13, column=1,padx=5,pady=5)
        e13.grid(row=14, column=1,padx=5,pady=5)
        e14.grid(row=15, column=1,padx=5,pady=5)
        e16.grid(row=17, column=1,padx=5,pady=5)
        e17.grid(row=18, column=1,padx=5,pady=5)
        e18.grid(row=19, column=1,padx=5,pady=5)
        e19.grid(row=20, column=1,padx=5,pady=5)
        e20.grid(row=21, column=1,padx=5,pady=5)
        e21.grid(row=22, column=1,padx=5,pady=5)
        d1={1:'Male',2:'Female'}
        var=IntVar()
        for i in d1:
            r=Radiobutton(new,text=d1[i],value=i,width=22,bg="#D6F5FF",command=None)
            r.grid(row=5,column=i)
        e6.grid(row=5,column=1,columnspan=3,padx=5,pady=5)
        var1 = IntVar()
        Checkbutton(new, text="General", variable=var1,bg="#D6F5FF").grid(row=7,column=1)
        var2 = IntVar()
        Checkbutton(new, text="SC", variable=var2,bg="#D6F5FF").grid(row=7,column=2)
        var3 = IntVar()
        Checkbutton(new, text="ST", variable=var3,bg="#D6F5FF").grid(row=8,column=1)
        var4= IntVar()
        Checkbutton(new, text="OBC", variable=var4,bg="#D6F5FF").grid(row=8,column=2)
        var6 = IntVar()
        Checkbutton(new, text="Hindu", variable=var6,bg="#D6F5FF").grid(row=9,column=1)
        var7 = IntVar()
        Checkbutton(new, text="Muslim", variable=var7,bg="#D6F5FF").grid(row=9,column=2)
        var8 = IntVar()
        Checkbutton(new, text="Christian", variable=var8,bg="#D6F5FF").grid(row=10,column=1)
        var9 = IntVar()
        Checkbutton(new, text="Others", variable=var9,bg="#D6F5FF").grid(row=10,column=2)
        new.mainloop()
    def last_5():
            admin_win2.destroy()
            def last_5_final(acc_no):
                last_5_win.destroy()
                fh=open('tot_userid.txt','r+')
                if '$'+acc_no+'$' in fh.read():
                    fh.seek(0)
                    for x in  fh.readlines():
                        splt=x.split('$')
                        if splt[1]==str(acc_no):
                            userid=(splt[2])
                else:
                    messagebox.showerror('Error','This Account no is not in our database ,Please check it')
                    return                 
                last_5=Tk()                
                last_5.geometry('390x295')
                last_5.maxsize(height=295,width=390)
                last_5.config(bg="#D6F5FF")
                last_5.title('Account Database')
                last_5.iconbitmap('bank.ico')
                def close():
                    last_5.destroy()
                close_but=Button(last_5,text='Close',command=close,anchor='center')
                close_but.pack(side='right')
                close_but.place(x=340,y=10)
                main=Label(last_5, text='Last 5 Transactions', anchor='center',font=('Bernard MT Condensed',16),bg="#D6F5FF",padx=15,pady=15 )
                main.pack()
                file=open('cust_data/'+userid+'/transaction.txt','r+')
                fh=file.readlines()
                bal=fh[-1]
                bal=bal.split('$')
                bal=bal[2]
                current_bal=Label(last_5, text='Current Balance:- '+bal+'.00', anchor='center',bg="#D6F5FF")
                current_bal.pack()
                current_bal.place(y=60,x=110)
                date=Label(last_5, text='Date',bg="#D6F5FF")
                date.pack()
                date.place(x=55,y=100)
                total_bal=Label(last_5, text='Current Balance',bg="#D6F5FF")
                total_bal.pack()
                total_bal.place(x=140,y=100)
                status=Label(last_5, text='Status',bg="#D6F5FF")
                status.pack()
                status.place(x=260,y=100)
                try:
                    data1=fh[-1]
                    data1=data1.split('$')
                    data1_label1=Label(last_5, text=data1[1],bg="#D6F5FF")
                    data1_label1.pack()
                    data1_label1.place(x=50,y=130)
                    data1_label2=Label(last_5, text=data1[2],bg="#D6F5FF")
                    data1_label2.pack()
                    data1_label2.place(x=150,y=130)
                    data1_label3=Label(last_5, text=data1[3]+'  '+data1[4],bg="#D6F5FF")
                    data1_label3.pack()
                    data1_label3.place(x=250,y=130)
                    data2=fh[-2]
                    data2=data2.split('$')
                    data2_label1=Label(last_5, text=data2[1],bg="#D6F5FF")
                    data2_label1.pack()
                    data2_label1.place(x=50,y=155)
                    data2_label2=Label(last_5, text=data2[2],bg="#D6F5FF")
                    data2_label2.pack()
                    data2_label2.place(x=150,y=155)
                    data2_label3=Label(last_5, text=data2[3]+'  '+data2[4],bg="#D6F5FF")
                    data2_label3.pack()
                    data2_label3.place(x=250,y=155)
                    data3=fh[-3]
                    data3=data3.split('$')
                    data3_label1=Label(last_5, text=data3[1],bg="#D6F5FF")
                    data3_label1.pack()
                    data3_label1.place(x=50,y=180)
                    data3_label2=Label(last_5, text=data3[2],bg="#D6F5FF")
                    data3_label2.pack()
                    data3_label2.place(x=150,y=180)
                    data3_label3=Label(last_5, text=data3[3]+' '+data3[4],bg="#D6F5FF")
                    data3_label3.pack()
                    data3_label3.place(x=250,y=180)
                    data4=fh[-4]
                    data4=data4.split('$')
                    data4_label1=Label(last_5, text=data4[1],bg="#D6F5FF")
                    data4_label1.pack()
                    data4_label1.place(x=50,y=205)
                    data4_label2=Label(last_5, text=data4[2],bg="#D6F5FF")
                    data4_label2.pack()
                    data4_label2.place(x=150,y=205)
                    data4_label3=Label(last_5, text=data4[3]+' '+data4[4],bg="#D6F5FF")
                    data4_label3.pack()
                    data4_label3.place(x=250,y=205)
                    data5=fh[-5]
                    data5=data5.split('$')
                    data5_label1=Label(last_5, text=data5[1],bg="#D6F5FF")
                    data5_label1.pack()
                    data5_label1.place(x=50,y=230)
                    data5_label2=Label(last_5, text=data5[2],bg="#D6F5FF")
                    data5_label2.pack()
                    data5_label2.place(x=150,y=230)
                    data5_label3=Label(last_5, text=data5[3]+' '+data5[4],bg="#D6F5FF")
                    data5_label3.pack()
                    data5_label3.place(x=250,y=230)
                except IndexError:
                    pass            
            last_5_win=Tk()
            last_5_win.config(bg="#D6F5FF")            
            last_5_win.title('History')
            last_5_win.iconbitmap('bank.ico')
            acc_label=Label(last_5_win,text='Enter Account Number',anchor='center',font=('PRIMETIME',15),bg="#D6F5FF")
            acc_label.pack(padx=15,pady=15)
            acc_entry=Entry(last_5_win,bd=5)
            acc_entry.pack(padx=5,pady=5)
            acc_cont=Button(last_5_win,text='Continue',command=lambda:last_5_final(acc_entry.get()))
            acc_cont.pack(padx=5,pady=5)   
    info=Label(admin_win2, text='Click the desired option', width=25, anchor='center',font=('Pricedown Bl',16),bg="#D6F5FF")
    info.pack()
    info.place(x=40,y=10)
    create=Button(admin_win2,text="Create Account",command=New)        
    create.pack()
    create.place(x=40,y=70)
    delete=Button(admin_win2,text="Delete Account",command=delete_account)
    delete.pack()
    delete.place(x=140,y=70)
    Transaction=Button(admin_win2,text="Transaction",command=transact)
    Transaction.pack()
    Transaction.place(x=240,y=70)
    Transaction_history=Button(admin_win2,text="Last 5 Transactions",command=last_5)
    Transaction_history.pack()
    Transaction_history.place(x=130,y=110)  
    admin_win2.mainloop()                

class Customer_win(object):
    def __init__(self):
        self.sign_in()
    def retrive_home(self):
        self.window.destroy()
        start=home_page()       
    def win_dow(self):
        self.window.destroy()
        start=after_sign_in_customer()
    def sign_in(self):
        self.window=Tk()
        self.window.config(bg="#D6F5FF")
        self.window.geometry('350x220')
        self.window.iconbitmap('bank.ico')
        
        self.window.maxsize(height=220,width=350)
        self.window.title('Welcome to Customer Login')
        def next():
            self.username=self.entry_check1.get()
            st=self.username
            password=self.entry_check2.get()
            if self.username=='' or password=='':
                messagebox.showerror('Error','Blank Username or Password')
                return
            fh=open('tot_userid.txt','r+')
            if '$'+self.username+'$' in fh.read():
                fh=open('cust_data/'+self.username+'/security'+'.txt','r+')
                password_verify=fh.readlines()[0]
                password_verify=password_verify.split('$')
                password_verify=password_verify[2]
                fh.close()
                fh=open('cust_data/'+self.username+'/acc_info'+'.txt','r+')
                name_user=fh.readlines()[0]                
                if password_verify==password:
                    i='Welcome Back'+ '  '+name_user
                    messagebox.showinfo('Welcome to Database',i)
                    self.window.destroy()
                    start=after_sign_in_customer(st)                
                else:
                    messagebox.showerror('Password Incorrect',self.username+' '+'Your Password in incorrect \nPlease Try Again')
            else:
                messagebox.showerror('Error','Invalid Login Please Check credentials')                
        user_id=Label(self.window,text='Enter Your User Id',bg="#D6F5FF")
        user_id.pack(padx=15,pady=5,anchor='center') 
        self.entry_check1=Entry(self.window,bd=5)
        self.entry_check1.pack(padx=15,pady=5,anchor='center')
        pwd=Label(self.window,text='Enter Your Password',bg="#D6F5FF")
        pwd.pack(padx=15,pady=5,anchor='center')
        self.entry_check2=Entry(self.window,bd=5,show='*')
        self.entry_check2.pack(padx=15,pady=5,anchor='center')
        button=Button(self.window,text='Sign In',command=next)
        button.pack(padx=5,side=RIGHT)
        button1=Button(self.window,text='Cancel',command=self.retrive_home)
        button1.pack(padx=5,side=LEFT)
        self.window.mainloop()

class credits_win(object):    
    def __init__(self):
        self.Credits=Tk()
        self.Credits.title("Credits")
        self.Credits.iconbitmap('bank.ico')
        self.Credits.geometry("522x320")
        self.Credits.maxsize(width=522,height=320)
        self.Credits.config(bg="#D6F5FF")
        credits_text='''
This project is an experimental approach towards making a Bank Database

      Here, "Python" language is used under complete development.

                        © All Rights Reserved

                         Thanks to python 3.4

                             Thanks

                        Have A Nice Day!
                                                            
'''
        text=Label(self.Credits,text=credits_text,bg="#D6F5FF",anchor='center')
        text.pack()
        text.place(x=50,y=50)
        self.Credits.mainloop()                   

class home_page(object):
    def __init__(self):
        homepage=Tk()
        homepage.title('PyBank')
        homepage.geometry('388x304')
        homepage.maxsize(height=304,width=388)
        homepage.iconbitmap('bank.ico')
        homepage.config(bg='#FFFFFF')        
        def Opt1():
            homepage.destroy()
            start=account()
        def Opt2():
            homepage.destroy()
            start=Customer_win()
        def Opt3():
            homepage.destroy()
            start=credits_win()
        def Opt4():
            homepage.destroy()
        logo = PhotoImage(file="bank.gif")
        logo_final= Label(homepage, image=logo,bg='#FFFFFF').pack(side='top')  
        Pybank=Label(text="PYBANK",font=('PRIMETIME',30),bg='#FFFFFF' )
        Pybank.pack()
        Pybank.place(y=100,x=100)
        admin_label=Label(text="Admin Login",bg='#FFFFFF')
        admin_label.pack(padx=10,pady=10)
        admin_label.place(x=100,y=180)
        admin_but=Button(text="Admin",command=Opt1)
        admin_but.pack()
        admin_but.place(x=110,y=210)
        customer_label=Label(text='Customer Login',bg='#FFFFFF')
        customer_label.pack(padx=10,pady=10)
        customer_label.place(x=220,y=180)
        customer_but=Button(text='Customer',command=Opt2)
        customer_but.pack()
        customer_but.place(x=235,y=210)
        credits_but=Button(text='Credits',command=Opt3)
        credits_but.pack()
        credits_but.place(x=110,y=250)
        exit_but=Button(text='Close',command=Opt4)
        exit_but.pack()
        exit_but.place(x=245,y=250)
        homepage.mainloop()        
start=home_page()
        
