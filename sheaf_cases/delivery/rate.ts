export function deliveryRate(delivered: number, attempted: number): number {
  if (delivered < 0 || attempted < 0 || delivered > attempted) {
    throw new Error("invalid delivery totals");
  }
  return attempted === 0 ? 0 : delivered / attempted;
}
