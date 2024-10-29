################################################################################
##
## This library is free software; you can redistribute it and/or
## modify it under the terms of the GNU Lesser General Public
## License as published by the Free Software Foundation; either
## version 2.1 of the License, or (at your option) any later version.
## 
## This library is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public
## License along with this library; if not, write to the Free Software
## Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
##
## (C) Copyrights Dr. Michel F. Sanner and TSRI 2016
##
################################################################################

from DejaVu.colorMap import ColorMap
from numpy import array
cm = ColorMap('bgr256')
cfg = {'name': 'bgr256', 'ramp': array([[ 1.        ,  0.        ,  0.        ,  1.        ],
       [ 1.        ,  0.        ,  0.        ,  1.        ],
       [ 1.        ,  0.024     ,  0.        ,  1.        ],
       [ 1.        ,  0.048     ,  0.        ,  1.        ],
       [ 1.        ,  0.048     ,  0.        ,  1.        ],
       [ 1.        ,  0.066     ,  0.        ,  1.        ],
       [ 1.        ,  0.09      ,  0.        ,  1.        ],
       [ 1.        ,  0.09      ,  0.        ,  1.        ],
       [ 1.        ,  0.114     ,  0.        ,  1.        ],
       [ 1.        ,  0.138     ,  0.        ,  1.        ],
       [ 1.        ,  0.138     ,  0.        ,  1.        ],
       [ 1.        ,  0.162     ,  0.        ,  1.        ],
       [ 1.        ,  0.18000001,  0.        ,  1.        ],
       [ 1.        ,  0.18000001,  0.        ,  1.        ],
       [ 1.        ,  0.204     ,  0.        ,  1.        ],
       [ 1.        ,  0.228     ,  0.        ,  1.        ],
       [ 1.        ,  0.228     ,  0.        ,  1.        ],
       [ 1.        ,  0.252     ,  0.        ,  1.        ],
       [ 1.        ,  0.27599999,  0.        ,  1.        ],
       [ 1.        ,  0.30000001,  0.        ,  1.        ],
       [ 1.        ,  0.30000001,  0.        ,  1.        ],
       [ 1.        ,  0.31799999,  0.        ,  1.        ],
       [ 1.        ,  0.34200001,  0.        ,  1.        ],
       [ 1.        ,  0.34200001,  0.        ,  1.        ],
       [ 1.        ,  0.366     ,  0.        ,  1.        ],
       [ 1.        ,  0.38999999,  0.        ,  1.        ],
       [ 1.        ,  0.38999999,  0.        ,  1.        ],
       [ 1.        ,  0.414     ,  0.        ,  1.        ],
       [ 1.        ,  0.43200001,  0.        ,  1.        ],
       [ 1.        ,  0.43200001,  0.        ,  1.        ],
       [ 1.        ,  0.456     ,  0.        ,  1.        ],
       [ 1.        ,  0.47999999,  0.        ,  1.        ],
       [ 1.        ,  0.47999999,  0.        ,  1.        ],
       [ 1.        ,  0.50400001,  0.        ,  1.        ],
       [ 1.        ,  0.528     ,  0.        ,  1.        ],
       [ 1.        ,  0.546     ,  0.        ,  1.        ],
       [ 1.        ,  0.546     ,  0.        ,  1.        ],
       [ 1.        ,  0.56999999,  0.        ,  1.        ],
       [ 1.        ,  0.59399998,  0.        ,  1.        ],
       [ 1.        ,  0.59399998,  0.        ,  1.        ],
       [ 1.        ,  0.61799997,  0.        ,  1.        ],
       [ 1.        ,  0.64200002,  0.        ,  1.        ],
       [ 1.        ,  0.64200002,  0.        ,  1.        ],
       [ 1.        ,  0.66000003,  0.        ,  1.        ],
       [ 1.        ,  0.68400002,  0.        ,  1.        ],
       [ 1.        ,  0.68400002,  0.        ,  1.        ],
       [ 1.        ,  0.708     ,  0.        ,  1.        ],
       [ 1.        ,  0.73199999,  0.        ,  1.        ],
       [ 1.        ,  0.73199999,  0.        ,  1.        ],
       [ 1.        ,  0.75599998,  0.        ,  1.        ],
       [ 1.        ,  0.77999997,  0.        ,  1.        ],
       [ 1.        ,  0.79799998,  0.        ,  1.        ],
       [ 1.        ,  0.79799998,  0.        ,  1.        ],
       [ 1.        ,  0.82200003,  0.        ,  1.        ],
       [ 1.        ,  0.84600002,  0.        ,  1.        ],
       [ 1.        ,  0.84600002,  0.        ,  1.        ],
       [ 1.        ,  0.87      ,  0.        ,  1.        ],
       [ 1.        ,  0.89399999,  0.        ,  1.        ],
       [ 1.        ,  0.89399999,  0.        ,  1.        ],
       [ 1.        ,  0.912     ,  0.        ,  1.        ],
       [ 1.        ,  0.93599999,  0.        ,  1.        ],
       [ 1.        ,  0.93599999,  0.        ,  1.        ],
       [ 1.        ,  0.95999998,  0.        ,  1.        ],
       [ 1.        ,  0.98400003,  0.        ,  1.        ],
       [ 1.        ,  0.98400003,  0.        ,  1.        ],
       [ 0.99199998,  1.        ,  0.        ,  1.        ],
       [ 0.97399998,  1.        ,  0.        ,  1.        ],
       [ 0.97399998,  1.        ,  0.        ,  1.        ],
       [ 0.94999999,  1.        ,  0.        ,  1.        ],
       [ 0.926     ,  1.        ,  0.        ,  1.        ],
       [ 0.90200001,  1.        ,  0.        ,  1.        ],
       [ 0.90200001,  1.        ,  0.        ,  1.        ],
       [ 0.87800002,  1.        ,  0.        ,  1.        ],
       [ 0.86000001,  1.        ,  0.        ,  1.        ],
       [ 0.86000001,  1.        ,  0.        ,  1.        ],
       [ 0.83600003,  1.        ,  0.        ,  1.        ],
       [ 0.81199998,  1.        ,  0.        ,  1.        ],
       [ 0.81199998,  1.        ,  0.        ,  1.        ],
       [ 0.78799999,  1.        ,  0.        ,  1.        ],
       [ 0.764     ,  1.        ,  0.        ,  1.        ],
       [ 0.764     ,  1.        ,  0.        ,  1.        ],
       [ 0.74000001,  1.        ,  0.        ,  1.        ],
       [ 0.722     ,  1.        ,  0.        ,  1.        ],
       [ 0.722     ,  1.        ,  0.        ,  1.        ],
       [ 0.69800001,  1.        ,  0.        ,  1.        ],
       [ 0.67400002,  1.        ,  0.        ,  1.        ],
       [ 0.64999998,  1.        ,  0.        ,  1.        ],
       [ 0.64999998,  1.        ,  0.        ,  1.        ],
       [ 0.62599999,  1.        ,  0.        ,  1.        ],
       [ 0.60799998,  1.        ,  0.        ,  1.        ],
       [ 0.60799998,  1.        ,  0.        ,  1.        ],
       [ 0.58399999,  1.        ,  0.        ,  1.        ],
       [ 0.56      ,  1.        ,  0.        ,  1.        ],
       [ 0.56      ,  1.        ,  0.        ,  1.        ],
       [ 0.53600001,  1.        ,  0.        ,  1.        ],
       [ 0.51200002,  1.        ,  0.        ,  1.        ],
       [ 0.51200002,  1.        ,  0.        ,  1.        ],
       [ 0.49399999,  1.        ,  0.        ,  1.        ],
       [ 0.47      ,  1.        ,  0.        ,  1.        ],
       [ 0.47      ,  1.        ,  0.        ,  1.        ],
       [ 0.44600001,  1.        ,  0.        ,  1.        ],
       [ 0.42199999,  1.        ,  0.        ,  1.        ],
       [ 0.398     ,  1.        ,  0.        ,  1.        ],
       [ 0.398     ,  1.        ,  0.        ,  1.        ],
       [ 0.38      ,  1.        ,  0.        ,  1.        ],
       [ 0.35600001,  1.        ,  0.        ,  1.        ],
       [ 0.35600001,  1.        ,  0.        ,  1.        ],
       [ 0.33199999,  1.        ,  0.        ,  1.        ],
       [ 0.308     ,  1.        ,  0.        ,  1.        ],
       [ 0.308     ,  1.        ,  0.        ,  1.        ],
       [ 0.28400001,  1.        ,  0.        ,  1.        ],
       [ 0.25999999,  1.        ,  0.        ,  1.        ],
       [ 0.25999999,  1.        ,  0.        ,  1.        ],
       [ 0.242     ,  1.        ,  0.        ,  1.        ],
       [ 0.21799999,  1.        ,  0.        ,  1.        ],
       [ 0.21799999,  1.        ,  0.        ,  1.        ],
       [ 0.19400001,  1.        ,  0.        ,  1.        ],
       [ 0.17      ,  1.        ,  0.        ,  1.        ],
       [ 0.17      ,  1.        ,  0.        ,  1.        ],
       [ 0.146     ,  1.        ,  0.        ,  1.        ],
       [ 0.12800001,  1.        ,  0.        ,  1.        ],
       [ 0.104     ,  1.        ,  0.        ,  1.        ],
       [ 0.104     ,  1.        ,  0.        ,  1.        ],
       [ 0.08      ,  1.        ,  0.        ,  1.        ],
       [ 0.056     ,  1.        ,  0.        ,  1.        ],
       [ 0.056     ,  1.        ,  0.        ,  1.        ],
       [ 0.032     ,  1.        ,  0.        ,  1.        ],
       [ 0.014     ,  1.        ,  0.        ,  1.        ],
       [ 0.014     ,  1.        ,  0.        ,  1.        ],
       [ 0.        ,  1.        ,  0.01      ,  1.        ],
       [ 0.        ,  1.        ,  0.034     ,  1.        ],
       [ 0.        ,  1.        ,  0.034     ,  1.        ],
       [ 0.        ,  1.        ,  0.058     ,  1.        ],
       [ 0.        ,  1.        ,  0.082     ,  1.        ],
       [ 0.        ,  1.        ,  0.082     ,  1.        ],
       [ 0.        ,  1.        ,  0.1       ,  1.        ],
       [ 0.        ,  1.        ,  0.124     ,  1.        ],
       [ 0.        ,  1.        ,  0.148     ,  1.        ],
       [ 0.        ,  1.        ,  0.148     ,  1.        ],
       [ 0.        ,  1.        ,  0.17200001,  1.        ],
       [ 0.        ,  1.        ,  0.19599999,  1.        ],
       [ 0.        ,  1.        ,  0.19599999,  1.        ],
       [ 0.        ,  1.        ,  0.22      ,  1.        ],
       [ 0.        ,  1.        ,  0.23800001,  1.        ],
       [ 0.        ,  1.        ,  0.23800001,  1.        ],
       [ 0.        ,  1.        ,  0.26199999,  1.        ],
       [ 0.        ,  1.        ,  0.28600001,  1.        ],
       [ 0.        ,  1.        ,  0.28600001,  1.        ],
       [ 0.        ,  1.        ,  0.31      ,  1.        ],
       [ 0.        ,  1.        ,  0.33399999,  1.        ],
       [ 0.        ,  1.        ,  0.33399999,  1.        ],
       [ 0.        ,  1.        ,  0.352     ,  1.        ],
       [ 0.        ,  1.        ,  0.37599999,  1.        ],
       [ 0.        ,  1.        ,  0.40000001,  1.        ],
       [ 0.        ,  1.        ,  0.40000001,  1.        ],
       [ 0.        ,  1.        ,  0.42399999,  1.        ],
       [ 0.        ,  1.        ,  0.44800001,  1.        ],
       [ 0.        ,  1.        ,  0.44800001,  1.        ],
       [ 0.        ,  1.        ,  0.46599999,  1.        ],
       [ 0.        ,  1.        ,  0.49000001,  1.        ],
       [ 0.        ,  1.        ,  0.49000001,  1.        ],
       [ 0.        ,  1.        ,  0.514     ,  1.        ],
       [ 0.        ,  1.        ,  0.53799999,  1.        ],
       [ 0.        ,  1.        ,  0.53799999,  1.        ],
       [ 0.        ,  1.        ,  0.56199998,  1.        ],
       [ 0.        ,  1.        ,  0.57999998,  1.        ],
       [ 0.        ,  1.        ,  0.57999998,  1.        ],
       [ 0.        ,  1.        ,  0.60399997,  1.        ],
       [ 0.        ,  1.        ,  0.62800002,  1.        ],
       [ 0.        ,  1.        ,  0.62800002,  1.        ],
       [ 0.        ,  1.        ,  0.65200001,  1.        ],
       [ 0.        ,  1.        ,  0.676     ,  1.        ],
       [ 0.        ,  1.        ,  0.69999999,  1.        ],
       [ 0.        ,  1.        ,  0.69999999,  1.        ],
       [ 0.        ,  1.        ,  0.71799999,  1.        ],
       [ 0.        ,  1.        ,  0.74199998,  1.        ],
       [ 0.        ,  1.        ,  0.74199998,  1.        ],
       [ 0.        ,  1.        ,  0.76599997,  1.        ],
       [ 0.        ,  1.        ,  0.79000002,  1.        ],
       [ 0.        ,  1.        ,  0.79000002,  1.        ],
       [ 0.        ,  1.        ,  0.81400001,  1.        ],
       [ 0.        ,  1.        ,  0.83200002,  1.        ],
       [ 0.        ,  1.        ,  0.83200002,  1.        ],
       [ 0.        ,  1.        ,  0.85600001,  1.        ],
       [ 0.        ,  1.        ,  0.88      ,  1.        ],
       [ 0.        ,  1.        ,  0.88      ,  1.        ],
       [ 0.        ,  1.        ,  0.90399998,  1.        ],
       [ 0.        ,  1.        ,  0.92799997,  1.        ],
       [ 0.        ,  1.        ,  0.94599998,  1.        ],
       [ 0.        ,  1.        ,  0.94599998,  1.        ],
       [ 0.        ,  1.        ,  0.97000003,  1.        ],
       [ 0.        ,  1.        ,  0.99400002,  1.        ],
       [ 0.        ,  1.        ,  0.99400002,  1.        ],
       [ 0.        ,  0.98199999,  1.        ,  1.        ],
       [ 0.        ,  0.958     ,  1.        ,  1.        ],
       [ 0.        ,  0.958     ,  1.        ,  1.        ],
       [ 0.        ,  0.94      ,  1.        ,  1.        ],
       [ 0.        ,  0.91600001,  1.        ,  1.        ],
       [ 0.        ,  0.91600001,  1.        ,  1.        ],
       [ 0.        ,  0.89200002,  1.        ,  1.        ],
       [ 0.        ,  0.86799997,  1.        ,  1.        ],
       [ 0.        ,  0.86799997,  1.        ,  1.        ],
       [ 0.        ,  0.84399998,  1.        ,  1.        ],
       [ 0.        ,  0.81999999,  1.        ,  1.        ],
       [ 0.        ,  0.80199999,  1.        ,  1.        ],
       [ 0.        ,  0.80199999,  1.        ,  1.        ],
       [ 0.        ,  0.778     ,  1.        ,  1.        ],
       [ 0.        ,  0.75400001,  1.        ,  1.        ],
       [ 0.        ,  0.75400001,  1.        ,  1.        ],
       [ 0.        ,  0.73000002,  1.        ,  1.        ],
       [ 0.        ,  0.70599997,  1.        ,  1.        ],
       [ 0.        ,  0.70599997,  1.        ,  1.        ],
       [ 0.        ,  0.68800002,  1.        ,  1.        ],
       [ 0.        ,  0.66399997,  1.        ,  1.        ],
       [ 0.        ,  0.66399997,  1.        ,  1.        ],
       [ 0.        ,  0.63999999,  1.        ,  1.        ],
       [ 0.        ,  0.616     ,  1.        ,  1.        ],
       [ 0.        ,  0.616     ,  1.        ,  1.        ],
       [ 0.        ,  0.59200001,  1.        ,  1.        ],
       [ 0.        ,  0.574     ,  1.        ,  1.        ],
       [ 0.        ,  0.574     ,  1.        ,  1.        ],
       [ 0.        ,  0.55000001,  1.        ,  1.        ],
       [ 0.        ,  0.52600002,  1.        ,  1.        ],
       [ 0.        ,  0.50199997,  1.        ,  1.        ],
       [ 0.        ,  0.50199997,  1.        ,  1.        ],
       [ 0.        ,  0.47799999,  1.        ,  1.        ],
       [ 0.        ,  0.46000001,  1.        ,  1.        ],
       [ 0.        ,  0.46000001,  1.        ,  1.        ],
       [ 0.        ,  0.43599999,  1.        ,  1.        ],
       [ 0.        ,  0.412     ,  1.        ,  1.        ],
       [ 0.        ,  0.412     ,  1.        ,  1.        ],
       [ 0.        ,  0.38800001,  1.        ,  1.        ],
       [ 0.        ,  0.36399999,  1.        ,  1.        ],
       [ 0.        ,  0.36399999,  1.        ,  1.        ],
       [ 0.        ,  0.34      ,  1.        ,  1.        ],
       [ 0.        ,  0.322     ,  1.        ,  1.        ],
       [ 0.        ,  0.322     ,  1.        ,  1.        ],
       [ 0.        ,  0.29800001,  1.        ,  1.        ],
       [ 0.        ,  0.27399999,  1.        ,  1.        ],
       [ 0.        ,  0.25      ,  1.        ,  1.        ],
       [ 0.        ,  0.25      ,  1.        ,  1.        ],
       [ 0.        ,  0.226     ,  1.        ,  1.        ],
       [ 0.        ,  0.208     ,  1.        ,  1.        ],
       [ 0.        ,  0.208     ,  1.        ,  1.        ],
       [ 0.        ,  0.184     ,  1.        ,  1.        ],
       [ 0.        ,  0.16      ,  1.        ,  1.        ],
       [ 0.        ,  0.16      ,  1.        ,  1.        ],
       [ 0.        ,  0.13600001,  1.        ,  1.        ],
       [ 0.        ,  0.112     ,  1.        ,  1.        ],
       [ 0.        ,  0.112     ,  1.        ,  1.        ],
       [ 0.        ,  0.094     ,  1.        ,  1.        ],
       [ 0.        ,  0.07      ,  1.        ,  1.        ],
       [ 0.        ,  0.07      ,  1.        ,  1.        ],
       [ 0.        ,  0.046     ,  1.        ,  1.        ],
       [ 0.        ,  0.022     ,  1.        ,  1.        ],
       [ 0.002     ,  0.        ,  1.        ,  1.        ]],'f'), 'maxi': 10.0, 'mini': 0.0}
cm.configure(*(), **cfg)
