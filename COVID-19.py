# Prog-12: COVID-19: The Latest Wave
# 6?3?????21 Name ?
import numpy as np
def read_data(filename):
 d = np.loadtxt(filename, delimiter=",", encoding='utf-8', dtype=str)
 new_cases = np.array(d[1:,1:], dtype=int)
 norm = new_cases / np.max(new_cases, axis=1).reshape((new_cases.shape[0],1))
 return {'new_cases': new_cases, 
 'norm_data': norm,
 'province_names': d[1:,0],
 'dates': d[0,1:]}


def max_new_cases_date(data):
    each_day = np.sum(data['new_cases'],axis =0 )
    result = list(each_day).index(np.max(each_day))
    return (data['dates'][result],np.max(each_day))


def max_new_cases_province(data, beg_date, end_date):
    beg = list(data['dates']).index(beg_date)
    end = list(data['dates']).index(end_date)
    new = data['new_cases'][:,beg:end+1]
    total = np.sum(new,axis=1)
    result = list(total).index(np.max(total))
    return  data['province_names'][result],np.max(total)
    

def max_new_cases_province_by_dates(data):
    a = np.ndarray((len(list(data['dates'])),3),dtype = object)
    b = np.ndarray((len(list(data['dates'])),1),dtype = object)
    a[:,0]=data['dates']
    a[:,2]=np.max(data['new_cases'],axis=0)
    b= np.argwhere(a[:,2]==data['new_cases'])
    bs=b[np.argsort(b[:,1])]
    a[:,1]=data['province_names'][bs[:,0]]
    return a


def most_similar(data, province):
    normprovince = data['norm_data'][list(data['province_names']).index(province)]
    normall=data['norm_data']
    np.delete(normall,np.argwhere(normall==normprovince))
    resultnorm = (normall - normprovince)**2
    lastresult=np.sum(resultnorm,axis=1)
    lastresult[np.argwhere(lastresult==0)]=lastresult.max()

    return data['province_names'][np.argwhere(lastresult==lastresult.min())][0][0]


def most_similar_province_pair(data):
    al = data['province_names']
    allnorm = data['norm_data']
    diff = (allnorm - allnorm.reshape(len(data['province_names']),1,len(data['dates'])))**2
    diff=np.sum(diff,axis=2)
    tester = np.identity(len(data['province_names']))*diff.max()
    diff += tester
    
    return (data['province_names'][np.argwhere(diff==diff.min())][0][0],data['province_names'][np.argwhere(diff==diff.min())][0][1])
    

def most_similar_in_period(data, province, beg_date, end_date):
    pass


def main():
 # put your own testing codes in this function
 data = read_data('TH_20210401_20210416.csv')       
 print(most_similar_province_pair(data))
main()
