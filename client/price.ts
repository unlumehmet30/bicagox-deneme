export async function getDisplayPrice(): Promise<string> {
  const response = await fetch("/price");
  const body = await response.json();
  const amount: number | null = body.amount;
  return amount === null ? "Unavailable" : amount.toFixed(2);
}
