import pandas as pd
import re
from pathlib import Path
from wavbench.report.plots.strategy import DispersionPlot
from wavbench.report.plots.appearance import (
    LegendPosition,
    AppearanceComposite,
    FacetGridAxisLabels,
)
from typing import List, Set, Dict, Any


def read(path_: str) -> pd.DataFrame:
    return pd.read_csv(path_)


def agg_csvs(dir_: str) -> None:
    partials = get_partials(dir_)
    for partial in partials:
        frames: List[pd.DataFrame] = read_list(
            get_files_by_partial(partial, dir_),
        )
        final_df: pd.DataFrame = create_agg_df(frames)

        final_df.to_csv(
            f"{dir_}/_final_{partial}.csv",
            index=False,
        )


def read_list(paths: List[Path]) -> List[pd.DataFrame]:
    return [read(filepath_.__str__()) for filepath_ in paths]


def get_partials(dir_: str) -> Set[str]:
    pattern: str = "^(?!_final)(.*?)(?:_\d{8}T\d{6})\.csv$"
    partials: Set[str] = set()

    for filepath_ in list(Path(dir_).glob("*.csv")):
        match = re.match(pattern, filepath_.name)
        if match:
            partials.add(match.group(1))

    return partials


def get_files_by_partial(partial_: str, dir_: str) -> List[Path]:
    return list(Path(dir_).glob(f"{partial_}*.csv"))


# =============================================================================

def create_agg_df(originals: List[pd.DataFrame]) -> pd.DataFrame:
    means: List[pd.DataFrame] = [
        group_by_with_mean(df, "provider_name")
        for df in originals
    ]

    final: pd.DataFrame = pd.DataFrame()

    for frame in means:
        final = merge(final, frame)

    return final


def merge(main: pd.DataFrame, branch_: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([main, branch_], ignore_index=True)


def group_by_with_mean(df_: pd.DataFrame, column: str) -> pd.DataFrame:
    return df_.groupby(column).apply(
        lambda group: pd.Series({
            "audio_duration": group["audio_duration"].mean(),
            "runtime": group["runtime"].mean(),
            "rtf": group["rtf"].mean(),
            "wer": group["wer"].mean(),
            "dataset_length": get_dataset_length(group),
            "audio_count": dataset_audio_count(group),
            "dataset": group["dataset"].iloc[0],
            "asr": group["ia"].iloc[0],
            'rtfx': (get_dataset_length(group) / group['runtime'].sum())
        }),
        include_groups=False
    ).round(3).reset_index()


def get_dataset_length(df_: pd.DataFrame) -> pd.Series:
    return df_["audio_duration"].sum()


def dataset_audio_count(df_: pd.DataFrame) -> int:
    return len(df_["audio"].unique())


if __name__ == "__main__":
    resource_dir: str = "./resources/final"
    w_dir: str = f"{resource_dir}/results-tcc-whisper"
    fw_dir: str = f"{resource_dir}/results-tcc-fasterwhisper"
    v_dir: str = f"{resource_dir}/results-tcc-vosk"

    # agg_csvs(w_dir)
    # agg_csvs(fw_dir)
    # agg_csvs(v_dir)

    # w_frames: List[pd.DataFrame] = read_list(
    #     get_files_by_partial("_final", w_dir),
    # )
    # fw_frames: List[pd.DataFrame] = read_list(
    #     get_files_by_partial("_final", fw_dir),
    # )
    # v_frames: List[pd.DataFrame] = read_list(
    #     get_files_by_partial("_final", v_dir),
    # )
    #
    # frames: List[pd.DataFrame] = w_frames + fw_frames + v_frames
    # agg_df: pd.DataFrame = pd.DataFrame()
    # results: List[Dict[str, Any]] = []
    #
    # for df in frames:
    #     agg_df = merge(agg_df, df)
    #
    # print(f"Agg: {agg_df}")
    #
    # providers = agg_df["provider_name"].unique()
    #
    # for provider in providers:
    #     p_agg: pd.DataFrame = agg_df[
    #         agg_df["provider_name"] == provider
    #         ].copy()
    #
    #     print()
    #     print(f"Pagg: {p_agg}")
    #
    #     length_sum = p_agg["dataset_length"].sum()
    #     wer_sum = (p_agg["wer"] * p_agg["dataset_length"]).sum()
    #     rtf_sum = (p_agg["rtfx"] * p_agg["dataset_length"]).sum()
    #
    #     print(f"Pagg After: {p_agg}")
    #
    #     result = {
    #         "provider_name": provider,
    #         "asr": p_agg["asr"].iloc[0],
    #         "wer": (wer_sum / length_sum) * 100,
    #         "rtfx": rtf_sum / length_sum,
    #     }
    #
    #     results.append(result)
    #
    # final_df: pd.DataFrame = pd.DataFrame(results).round(3)

    final_df: pd.DataFrame = read("./resources/final/final_agg.csv")

    strategy = DispersionPlot(
        x="wer",
        y="rtfx",
        hue="provider_name",
    )

    plot = strategy.plot(final_df)

    appearance_kit: AppearanceComposite = AppearanceComposite()
    appearance_kit.add(LegendPosition(plot))
    appearance_kit.add(
        FacetGridAxisLabels(
            plot=plot,
            xlabel="WER(%)",
            ylabel="RTFx",
            font_size=11.0,
        )
    )
    appearance_kit.customize()

    plot.savefig("./resources/final/final_plot.png", dpi=300, format="png")
    # final_df.to_csv("./resources/final/final_agg.csv", index=False)
