# coding:utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.mime.application import MIMEApplication 
from email.MIMEBase import MIMEBase
from email import Utils,Encoders
from email.utils import parseaddr, formataddr
import smtplib
import sys
print 'send email begin'
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

#from_addr = raw_input('From: ')
#password = raw_input('Password: ')
#to_addr = raw_input('To: ')
#smtp_server = raw_input('SMTP server: ')
from_addr = "hsgene_todaysoft@163.com"
password = "hsgene123"
#to_addr = "zj_bupt@sina.com"
#to_addr = ["zj_bupt@sina.com","zhangjing@hsgene.com","1094253356@qq.com","hsgene_todaysoft@163.com"]
#to_addr = sys.argv[1]
to_addr = []
f = open('test.txt','r')
for ln in f:
	if ln in to_addr:
		continue
	to_addr.append(ln)
f.close()
smtp_server = 'smtp.163.com'


#text
msg = MIMEMultipart('alternative')
#part = MIMEText('�õ�', 'plain', 'utf-8')
#html
msg = MIMEText('''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>Demystifying Email Design</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
 </head>
 <body style="margin: 0; padding: 0;">
  <table border="0" cellpadding="0" cellspacing="0" width="100%">
   <tr>
    <td style="padding: 20px 0 30px 0;">
     <table  style="border: 1px solid #cccccc;" align="center" cellpadding="0" cellspacing="0" width="600">
	  <!-- Part 1 -->
	  <tr>
       <td align="center" bgcolor="#ffffff" style="padding: 0 0 0 0;">
        <img src="http://a1.qpic.cn/psb?/V143Ct1g1kfnFK/WMH94R5NtlUFgRfFc1qvvaE**KOICN8lJ5S6HZICA2A!/m/dKwAAAAAAAAAnull&bo=sASnAAAAAAAFBzc!&rf=photolist&t=5" alt="���˵ļ��������ŵķ��񣬴�����ʻ�Ʒ��" width="600" height="100" style="display: block;" />
	   </td>
      </tr>
	  
	  <!-- Part 2 -->
	  <tr>
       <td bgcolor="#ffffff" style="padding: 40px 30px 40px 30px;">
        <table border="0" cellpadding="0" cellspacing="0" width="100%">
         <tr>
          <td style="color: #153643; font-family: Arial, sans-serif; font-size: 16px;">
		  <p>���������Ϊ�������ݷ�����һ��Īչ�����������Ϊʵ�����ݵ���ʵ�Զ��ɻ�������Բ���˾�����ݷ��������⣬����������Խ������ݷ������޴����֣��������õ���Ϊרҵ�����ݷ������񡭡�</p>
		  <p>��ô������ע���ǵĲ�Ʒ��</p>
          <p>����������ҵ�Ƽ����޹�˾��һ��רҵ����Ӧ������Ƽ�����з������ơ����ݷ����ĸ��¿Ƽ���ҵ��������SoftGenetics���ڹ��ʽ�������������ϵ�л�����������������ǵĲ�Ʒ��<font color="#FF0000">�����������ݷ�������NextGene?��Sanger�������ݷ������Mutation Surveyor?��DNAƬ�η������GeneMarker?</font>����ϵ��������м򵥡�ֱ�ۡ����ӻ��Ľ�����ʾ�����������û�������Ϣѧ������Ҫ��Ϊҽ��������ѧ�ҡ���������̵��ṩ����õ�ѡ�񡣴������ǻ���չ����������ݷ���ҵ�񡢲����������Ķ��ƿ�����Ϊ���ṩ�������ȵ�����������Ƽ����ݷ�������</p>
          <p>ȫ���г���4000��DNAʵ���Һ��о�����ʹ�ù�˾�з���DNA�������ݷ���ϵ�����������Ү³��ѧҽѧԺ��ͯ�����о����ġ�����·��ά��֢�Ŵ����������ġ�����Լ�����ս�˹��ѧ��֢�о������й���ѧԺ�����������о���������?Nat`l���������о���������?���ҿ�ѧ�о����ġ��¹�?Bioglobe����۴�ѧ���Ĵ�����?Anzac Health�ȵȡ���Щ�о��������������綥����ѧ��־���硶Nature���͡�Science�����ϵ������ر�ָ�����ڿ��й����У�����˾�������Ʒ������Ҫ�����á�</p>
          </td>
         </tr>
		 <tr>
          <td style="padding: 20px 0 0 0;color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;"">
		  1.<font color="#FF0000">NextGene?</font>����<a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0914/13.html">�����������ݷ�������</a>
			<p>NextGENe ?�ṩ����һ�����ģ������򹤳̵���������������������ʵ������װ������бȶԣ�NextGENe��Windows����ϵͳ���У�Ч�ʸߣ�׼ȷ�Ըߣ��û�����߱��ű���������������Ϣѧ��������Ӧ�á����Ҿ߱�ǿ��Ľ�����ʾ�ͱ���������ܣ����Է������бȶԽ�����鿴������Ϣ�ȡ��ɷ���Ion Torrent ����ƽ̨��Roche����ƽ̨��Illumina ����ƽ̨��SOLiD����ϵͳ������ԭʼ�������ݣ��ɼ���BAM��FASTQ��FASTA��CSFASTA�ȶ������ݸ�ʽ��</p>
          </td>
         </tr>
		 <tr>
          <td>
            <table border="0" cellpadding="0" cellspacing="0" width="100%">             
			 <tr>              
			  <td width="300" valign="middle">
				 <table border="0" cellpadding="0" cellspacing="0" width="100%">
				  <tr>
                   <td>
				   <a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0914/13.html">
                   <img src="http://a3.qpic.cn/psb?/V143Ct1g1kfnFK/hFlWHwWqXuYLha7QjPKJSIeaoaIGkzjBrh8ses3Eab4!/m/dKYAAAAAAAAAnull&bo=vwG0AQAAAAADByk!&rf=photolist&t=5" alt="" width="100%" height="400" style="display: block;" />
                   </a>
				   </td>
                  </tr>                 
                 </table>
              </td>
			  <td width="240">
			   <table border="0" cellpadding="0" cellspacing="0" width="100%">
                 <tr>
                  <td>
                    <ul>
					<font color="#FF0000" size="2px">��ҪӦ��:</font>
						<li><a href="http://www.softgenetics.com/NextGENe_01.php"><font size="2px">���������̬�ԣ�SNP��/����ȱʧ��InDel��</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_013.php"><font size="2px">���������죨CNV������</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_014.php"><font size="2px">��ϸ��ͻ����</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_03.php"><font size="2px">ȫ������ȶԼ�ͻ����</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_04.php"><font size="2px">RNA����/ת¼��������</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_07.php"><font size="2px">Ŀ�����򲶻����/�ز������</font]></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_18.php"><font size="2px">HLA����</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_08.php"><font size="2px">������ݼ�����������ҽ��</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_06.php"><font size="2px">reads��װ/Paired-endƴ��</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_05.php"><font size="2px">miRNA�ķ��ּ���������</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_02.php"><font size="2px">��������������Ԥ��</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_016.php"><font size="2px">��ϵ����������̵ıȶԷ���</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_017.php"><font size="2px">�ɵ��������ݿ�</font></a></li>
					</ul>
                  </td>
                 </tr>
                </table>
              </td>   
             </tr>
            </table>
          </td>
         </tr>
         <tr>
          <td style="padding: 20px 0 0 0;color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;"">
		  2.<font color="#FF0000">Mutation Surveyor?</font>����<a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0914/11.html">Sanger�������ݷ������</a>
		  <p>Mutation Surveyor?�ǻ���ͻ��(Mutation) �����������Լ�ⴿ���ӱ���(Homozygote)����SNP������/ȱʧ(InDel)���Ӻ��ӱ���(Heterozygote)����SNP������/ȱʧ(InDel)�ȡ����ɺͱ�׼���бȽϣ������ҳ���������ͼ�������еĻ������㡣</p>
          <p>Mutation Surveyor?��ͻ�����������������������״���������������߼�����׼ȷʶ�����/ȱʧ�Ӻ���ͻ�似����</p>
		  <p>����ϵͳ��֧�� Windows XP��Windows Vista��Windows 7����������ϵͳ��</p>
		  <p>���ݸ�ʽ��ABI��AB1��SCF�ļ�</p>
		  </td>
         </tr>
		 <tr>
          <td>
            <table border="0" cellpadding="0" cellspacing="0" width="100%">
			 
			 <tr>
			  <td width="300" valign="middle">
				 <table border="0" cellpadding="0" cellspacing="0" width="100%">
				  <tr>
                   <td>
				   <a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0914/11.html">
                   <img src="http://a4.qpic.cn/psb?/V143Ct1g1kfnFK/zf5zakWOZMECvSXts9vdxKPb8PKrZeIaaLUOelYhPcE!/m/dKsAAAAAAAAAnull&bo=gAKnAgAAAAADBwU!&rf=photolist&t=5" alt="" width="100%" height="300" style="display: block;" />
                   </a>
				   </td>
                  </tr>
                 
                 </table>
              </td> 
			  <td width="240">
			   <table border="0" cellpadding="0" cellspacing="0" width="100%">
                 <tr>
                  <td>
                    <ul>
					<font color="#FF0000" size="2px">��ҪӦ��:</font>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_1.php"><font size="2px">���������Ⱥ;���</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_2.php"><font size="2px">����INDEL���</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_3.php"><font size="2px">�Ӻ�INDEL���</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_4.php"><font size="2px">��ϸ��ͻ����</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_5.php"><font size="2px">ͻ����������</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_6.php"><font size="2px">�׻�������</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_11.php"><font size="2px">�Զ��屨��ѡ��</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_13.php"><font size="2px">������DNA���з���</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_14.php"><font size="2px">���˲���</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_15.php"><font size="2px">����ӱ������֪ʶ��</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_16.php"><font size="2px">�û��������Ƹ���</font></a></li>
					</ul>
                  </td>
                 </tr>
                </table>
              </td>   
             </tr>
            </table>
          </td>
		 </tr>
		 <tr>
          <td style="padding: 20px 0 0 0;color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;"">
		  3. <font color="#FF0000">GeneMarker?</font>����<a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0914/12.html">DNAƬ�η������</a>
		  <p>GeneMarker?�����ΨһΪ�����о�����Ƶġ�����ѧ���Ѻá��Ļ������������㷺Ӧ�����Ŵ�������������ҽ��ũ�����ֵ�������о��������������������ܲ��Ҳ���ֱ�ۣ�ʹ�÷ǳ���㣬������ʮ���Ӧ�ã���һ�ȷ�����١��Ѻá�����ǿ����Զ������ݷ��������</p>
		  </td>
         </tr>
		 <tr>
          <td>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"> 
			 <tr>
			  <td width="300" valign="middle">
				 <table border="0" cellpadding="0" cellspacing="0" width="100%">
				  <tr>
                   <td>
				   <a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0914/12.html">
                   <img src="http://a4.qpic.cn/psb?/V143Ct1g1kfnFK/e*bf8z77IiNbTjAo5hlFQb*3wDXLCJ7sLpSTS.2Kqgc!/m/dP8AAAAAAAAAnull&bo=7AJdAgAAAAAFB5U!&rf=photolist&t=5" alt="" width="100%" height="300" style="display: block;" />
                   </a>
				   </td>
                  </tr>
                 
                 </table>
              </td>
			  <td width="240">
			   <table border="0" cellpadding="0" cellspacing="0" width="100%">
                 <tr>
                  <td>
                    <ul>
					<font color="#FF0000" size="2px">��ҪӦ��:</font>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/1125/232.html"><font size="2px">STR(SSR��΢����) ���ݷ���</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/1108/189.html"><font size="2px">AFLP���ݷ���</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/0927/65.html"><font size="2px">MLPA?���ݷ���</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/1103/180.html"><font size="2px">������֢����</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/1123/225.html"><font size="2px">΢���ǲ��ȶ��ԣ�MSI������</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/1125/232.html"><font size="2px">�Ŵ���ϵ��ͼ���ϵ¶�����</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/1103/179.html"><font size="2px">�Ӻ���ȱʧ��LOH������</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0926/52.html"><font size="2px">��ҽ����Ե�����о�</font></a></li>
						<li><font size="2px">��ͨ��SNP����</font></li>
					</ul>
                  </td>
                 </tr>
                </table>
              </td> 
			  
             </tr>
            </table>
          </td>
         </tr>
		 <tr>
          <td style="padding: 20px 0 0 0;">
		   <p style="color: #FF0000; font-family: Arial, sans-serif; font-size: 24px;">������Ϣ��������</p>
		   <p style="color: #153643; font-family: Arial, sans-serif; font-size: 18px;padding: 0 0 0 0;">����ǿ���������Ϣ����ƽ̨����Ŀ����ḻ��������Ϣ�Ŷӣ�����нӲ���ԭʼ���ݵ�������Ϣ��������һ���������ݡ������������ݣ���������Ϣ������Ա���û�һ��һ�������ṩ���Ի������ݷ���������������Ӧ�û������󡣸����û��ķ���Ҫ������ʺϵ����ݷ���������</p>
          </td>
         </tr>
		 <tr>
          <td style="padding: 20px 0 0 0;">
		   <p style="color: #FF0000; font-family: Arial, sans-serif; font-size: 24px;">������ƿ�����</p>
		   <p style="color: #153643; font-family: Arial, sans-serif; font-size: 18px;padding: 0 0 0 0;">����ḻ����������Ŷ������и���ǿ��ķ�������Ļ����ϣ�������������ɫ���ܵ�ʵ�֡����ݷ���ƽ̨�Ĺ������Զ�������Ŀ����������ʵ�֣��ڲ������ݷ�����ƽ̨������������һ��֮����</p>
          </td>
         </tr>
		</table>
       </td>
      </tr>
	  
	  <!-- Part 3 -->
	  <tr>
       <td bgcolor="#778899" style="padding: 30px 30px 30px 30px;">
        <table border="0" cellpadding="0" cellspacing="0" width="100%">
         <tr>
		  <td style="font-family: Arial, sans-serif; font-size: 14px;">
			������Ϣ����ʣ�<br/>http://www.todaysoft.com.cn/ or http://www.softgenetics.com/<br/>
			��ϵ�绰��010-82600675   010-51197773-8131 <br/>
			���䣺liuyue@todaysoft.com.cn  yanzhenchen@hsgene.com <br/>
			��ַ�������йش嶫·18�Ų��ǹ��ʴ���C��15�� <br/>
			<a href="#" style="color: #ffffff;"><font color="#0000CD">Unsubscribe</font></a> to this newsletter instantly<br/>
			<span> ע�����˶���t��</span>
		  </td>
		  <td>
           <table border="0" cellpadding="0" cellspacing="0">
            <tr>
             <td>
              <a href="">
              <img src="http://a4.qpic.cn/psb?/V143Ct1g1kfnFK/0p6P1JQ6.RqyjEy093iAYhUVu3VuG8a2wkQoMtzJiyU!/m/dKsAAAAAAAAAnull&bo=NAISAwAAAAAFBwM!&rf=photolist&t=5" alt="��ά��" width="100" height="100" style="display: block;" border="0" />
              </a>
             </td>
            </tr>
           </table>
		  </td>
         </tr>
		</table>
       </td>
      </tr>
     </table>
    </td>
   </tr>
  </table>
 </body>
</html>''', 'html', _charset='GBK')

#attatchment
#msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python <%s>' % from_addr)
msg['To'] = _format_addr(u'<%s>' % to_addr)
#msg['To'] = ",".join(to_addr)
msg['Subject'] = Header(u'sayhello', 'utf-8').encode()
#msg["Accept-Language"]="zh-CN"
#msg["Accept-Charset"]="ISO-8859-1,utf-8"
#text part
#msg.attach(MIMEText('�õ�', 'plain', 'utf-8'))


#attatchment part  ����1 ͼƬ
#'''with open('E:\\test.jpg', 'rb') as f:
    # ���ø�����MIME���ļ�����������jpg����:
 #   mime = MIMEBase('image', 'jpg', filename='test.jpg')
    # ���ϱ�Ҫ��ͷ��Ϣ:
  #  mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
   # mime.add_header('Content-ID', '<0>')
    #mime.add_header('X-Attachment-Id', '0')
    # �Ѹ��������ݶ�����:
    #mime.set_payload(f.read())
    # ��Base64����:
    #encoders.encode_base64(mime)
    #��ͼƬ��������
    #msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    #	'<p><img src="cid:0"></p>' +
    #	'</body></html>', 'html', 'utf-8'))
    # ��ӵ�MIMEMultipart:
    #msg.attach(mime)
#attatchment part 
#part = MIMEApplication(open('E:\\test.txt','rb').read())  
#part.add_header('Content-Disposition', 'attachment', filename="test.txt")  
#msg.attach(part)'''
    
#���Ĵ���
server = smtplib.SMTP(smtp_server, 25)
#���ܴ��� �˿ڴ�C:\Anaconda2\Lib\smtplib.py  line 58����
#server = smtplib.SMTP(smtp_server,465)
#server = smtplib.SMTP_SSL(smtp_server, 465 )
#server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string().encode('ascii'))
server.quit()
