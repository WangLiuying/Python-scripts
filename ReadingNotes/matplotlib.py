# -*- coding: utf-8 -*-
"""
learning matplotlib
reference: Chen Qian.

Created on Thu Apr  5 10:40:42 2018

@author: Liuying Wang
"""

import numpy as np
import matplotlib.pyplot as plt

#%%切换风格
plt.style.use('ggplot')
plt.rcParams#默认参数
plt.rcParams['axes.prop_cycle']
#%%四宫格
fig,axes = plt.subplots(2,2,figsize = (9,7))
ax1,ax2,ax3,ax4 = axes.ravel()

#第一张图:散点图
x,y = np.random.normal(size = (2,100))
ax1.plot(x,y,'o') #plot默认散点图，scatter气泡图
ax1.set_title('Scatter Plot')


#第二张:正余弦
x = np.linspace(0,2,100)
for shift in np.linspace(0,2,5):
    ax2.plot(x,np.sin((x+shift)*np.pi),'-')
ax2.set_title('Curve')

#第三张：条形图
#x1,x2 = np.random.randint(low = 0, high = 100, size = (2,100))
#ax3.hist((x1,x2),bins = 10, labels = list('AB'),histtype = 'bar')
x = np.arange(5)
y1, y2 = np.random.randint(1, 25, size=(2, 5))
ax3.bar(x,y1,width = 0.3, color = '#E24A33')
ax3.bar(x+0.3,y2, width = 0.3, color = '#348ABD')
ax3.set_title('Bar Plot')

#第四张：画圆圈
for i, color in enumerate(plt.rcParams['axes.prop_cycle']):
    xy = np.random.normal(0.5,1,size = 2)
    ax4.add_patch(plt.Circle(xy,radius = 0.2, color = color['color']))
ax4.axis('equal')#调整轴
ax4.set_title('Bubles')

plt.show()

#%%另一种风格
plt.style.use('dark_background')
fig,ax = plt.subplots()

x = np.linspace(0,2,50)
for shift in np.linspace(0,2,5):
    ax.plot(x,np.sin((x+shift)*np.pi),'o-')
ax.set_title('Curve')

plt.show()

#%%灰底黑背

plt.style.use('bmh')

x = np.random.beta(1,1,size = 300)
x1 = np.random.beta(1,2,size = 300)
fig,ax = plt.subplots()
ax.hist(x,bins = 20,histtype = 'step')
ax.hist(x1,bins = 20, histtype = 'step')
plt.show()


#%%一个比较长的示例
import matplotlib.pyplot as plt
from matplotlib.mlab import csv2rec
from matplotlib.cbook import get_sample_data

#fname = get_sample_data('percent_bachelors_degrees_women_usa.csv')
#gender_degree_data = csv2rec(fname)

# These are the colors that will be used in the plot
color_sequence = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
                  '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
                  '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f',
                  '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']

# You typically want your plot to be ~1.33x wider than tall. This plot
# is a rare exception because of the number of lines being plotted on it.
# Common sizes: (10, 7.5) and (12, 9)
fig, ax = plt.subplots(1, 1, figsize=(12, 14))

# Remove the plot frame lines. They are unnecessary here.
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Ensure that the axis ticks only show up on the bottom and left of the plot.
# Ticks on the right and top of the plot are generally unnecessary.
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

fig.subplots_adjust(left=.06, right=.75, bottom=.02, top=.94)
# Limit the range of the plot to only where the data is.
# Avoid unnecessary whitespace.
ax.set_xlim(1969.5, 2011.1)
ax.set_ylim(-0.25, 90)

# Make sure your axis ticks are large enough to be easily read.
# You don't want your viewers squinting to read your plot.
plt.xticks(range(1970, 2011, 10), fontsize=14)
plt.yticks(range(0, 91, 10), fontsize=14)
ax.xaxis.set_major_formatter(plt.FuncFormatter('{:.0f}'.format))
ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}%'.format))

# Provide tick lines across the plot to help your viewers trace along
# the axis ticks. Make sure that the lines are light and small so they
# don't obscure the primary data lines.
plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)

# Remove the tick marks; they are unnecessary with the tick lines we just
# plotted.
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='on', left='off', right='off', labelleft='on')

# Now that the plot is prepared, it's time to actually plot the data!
# Note that I plotted the majors in order of the highest % in the final year.
majors = ['Health Professions', 'Public Administration', 'Education',
          'Psychology', 'Foreign Languages', 'English',
          'Communications\nand Journalism', 'Art and Performance', 'Biology',
          'Agriculture', 'Social Sciences and History', 'Business',
          'Math and Statistics', 'Architecture', 'Physical Sciences',
          'Computer Science', 'Engineering']

y_offsets = {'Foreign Languages': 0.5, 'English': -0.5,
             'Communications\nand Journalism': 0.75,
             'Art and Performance': -0.25, 'Agriculture': 1.25,
             'Social Sciences and History': 0.25, 'Business': -0.75,
             'Math and Statistics': 0.75, 'Architecture': -0.75,
             'Computer Science': 0.75, 'Engineering': -0.25}

for rank, column in enumerate(majors):
    # Plot each line separately with its own color.
    column_rec_name = column.replace('\n', '_').replace(' ', '_').lower()

    line = plt.plot(gender_degree_data.year,
                    gender_degree_data[column_rec_name],
                    lw=2.5,
                    color=color_sequence[rank])

    # Add a text label to the right end of every line. Most of the code below
    # is adding specific offsets y position because some labels overlapped.
    y_pos = gender_degree_data[column_rec_name][-1] - 0.5

    if column in y_offsets:
        y_pos += y_offsets[column]

    # Again, make sure that all labels are large enough to be easily read
    # by the viewer.
    plt.text(2011.5, y_pos, column, fontsize=14, color=color_sequence[rank])

# Make the title big enough so it spans the entire plot, but don't make it
# so big that it requires two lines to show.

# Note that if the title is descriptive enough, it is unnecessary to include
# axis labels; they are self-evident, in this plot's case.
fig.suptitle('Percentage of Bachelor\'s degrees conferred to women in '
             'the U.S.A. by major (1970-2011)\n', fontsize=18, ha='center')

# Finally, save the figure as a PNG.
# You can also save it as a PDF, JPEG, etc.
# Just change the file extension in this call.
# plt.savefig('percent-bachelors-degrees-women-usa.png', bbox_inches='tight')
plt.show()
#%%heatmap
import matplotlib.colors as mcolors
plt.style.use('ggplot')
data = np.vstack([
    np.random.multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    np.random.multivariate_normal([30, 20], [[2, 0.3], [0.3, 4]], size=1000)
])

gammas = [0.8,0.5,0.3]

fig,axes = plt.subplots(2,2)

ax1,ax2,ax3,ax4 = axes.ravel()

ax1.hist2d(data[:,0],data[:,1],bins = 100)
ax1.set_title('linear kernel')

for ax,gamma in zip(axes.ravel()[1:],gammas):
    ax.set_title('PowerNorm($\gamma = %s$)' % gamma)
    ax.hist2d(data[:,0],data[:,1],bins = 100, norm = mcolors.PowerNorm(gamma))

    
fig.tight_layout()
plt.show()


#%%加边图
from mpl_toolkits.axes_grid1 import make_axes_locatable
# the random data
x = np.random.randn(1000)
y = np.random.randn(1000)

#主散点图
fig,ax = plt.subplots(figsize = (9,9))
ax.scatter(x,y)
ax.set_aspect(1.)

#加入两个额外的边图
divider = make_axes_locatable(ax)
axtop = divider.append_axes('top',size = 1.2, pad = 0.1, sharex = ax)
axright = divider.append_axes('right',size = 1.2,pad = 0.1, sharey = ax)

axtop.hist(x,bins = 20)
axright.hist(y,bins = 20,orientation = 'horizontal')

#隐去没用的轴
plt.setp(axtop.get_xticklabels()+axright.get_yticklabels(),visible = False)

plt.show()

#%%stackplot

x1 = range(10)
y = np.row_stack([np.random.randint(5,25,10),np.random.randint(5,25,10),np.random.randint(5,25,10)])

plt.stackplot(x1,y)

#%%
