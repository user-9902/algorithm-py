const heap_sort = (arr) => {
  const n = arr.length;
  const heapify = (arr, n, i) => {
    const l = 2 * i + 1;
    const r = l + 1;

    const lagestIdx = i;
    if (l < n && arr[l] > arr[lagestIdx]) {
      lagestIdx = l;
    }
    if (r < n && arr[r] > arr[lagestIdx]) {
      lagestIdx = r;
    }
    if (lagestIdx !== i) {
      const tmp = arr[lagestIdx];
      arr[lagestIdx] = arr[i];
      arr[i] = tmp;
      heapify(arr, n, lagestIdx);
    }
  };
  // 堆化
  for (let i = n - 1; i > -1; i--) {
    heapify(arr, n, i);
  }

  // 每次，取最大的元素置于末尾，再整理下堆
  for (let i = 0; i < n; i++) {
    const tmp = arr[n - 1 - i];
    arr[n - 1 - i] = arr[i];
    arr[i] = tmp;
    heapify(arr, n - i, 0);
  }
};
