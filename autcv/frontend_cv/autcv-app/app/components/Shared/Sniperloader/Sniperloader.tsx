// app\components\Shared\SnipperLoader\Sniperloader.tsx
export function SniperLoading() {
  return (
    <div className="flex items-center justify-center h-screen bg-transparent">
      <div className="relative">
        <div
          className="w-16 h-16 border-4 border-gray-300 rounded-full animate-spin"
          aria-label="Cargando sesión segura"
        ></div>
      </div>
    </div>
  );
}
