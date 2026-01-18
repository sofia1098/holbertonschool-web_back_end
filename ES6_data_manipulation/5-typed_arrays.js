export default function createInt8TypedArray(length, position, value) {
  // Check if the position is within the bounds of the array length
  if (position >= length || position < 0) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);

  view.setInt8(position, value);

  return view;
}