export async function getDisplayPrice(): Promise<string> {
  const response = await fetch("/price");
  const body = await response.json();
  const amount: number = body.amount;
  return amount.toFixed(2);
}
