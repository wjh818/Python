import numpy as np
import pandas as pd

# 피벗테이블
# data = pd.DataFrame(np.arange(6).reshape(2, 3),
#                     index=pd.Index(['Ohio', 'Colorado'], name='state'),
#                     columns=pd.Index(['one', 'two', 'three'], name='number'))
# print(data)
#
#
# result = data.stack()       # 컬럼이 로우로 피벗됨
# print(result)
#
# print(result.unstack())     # 다시 원래대로
#
# print(result.unstack(0))
# print(result.unstack('state'))


###################################################################################################


# 그래프 시각화

import matplotlib.pyplot as plt
import numpy as np


# data = np.arange(10)
# print(data)
# plt.plot(data)
# plt.show()


fig =plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.plot(np.random.randn(50).cumsum(), 'k--')
_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30)+3*np.random.randn(30))
plt.show()

































































































































