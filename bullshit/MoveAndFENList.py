package GameFoundation;

import java.util.ArrayList;

/**
 * Created by richardwang007 on 3/31/17.
 */
public class MoveAndFENList {
    private ArrayList<Move> moveArrayList;
    private ArrayList<String> FENArrayList;

    public MoveAndFENList ()
    {
        moveArrayList = new ArrayList<>(30);
        FENArrayList = new ArrayList<>(30);
    }

    public ArrayList<Move> getMoveArrayList ()
    {
        return moveArrayList;
    }

    public void addMove(Move move)
    {
        moveArrayList.add(move);
    }

    public ArrayList<String> getFENArrayList()
    {
        return FENArrayList;
    }

    public void addFEN(String fen)
    {
        FENArrayList.add(fen);
    }

    /**
     * detects a draw by threefold repetition
     * @return true if the game is drawn; otherwise,
     *         false
     */
    public boolean isDrawnByThreefoldRepetition()
    {
        if (FENArrayList.size()>=6)
        {
            for (int i = 0; i<FENArrayList.size()-1; i++)
            {
                int counter = 0;
                for (int j=i+1; j<FENArrayList.size(); j++)
                {
                    if (this.cutFEN(FENArrayList.get(i)).equals(this.cutFEN(FENArrayList.get(j))))
                        counter++;
                }
                if (counter>=3)
                    return true;
            }
        }
        return false;
    }

    /**
     * cuts the fen string to a strictly positional standpoint
     * @return a string denoting the position
     * @param fen has to be a FEN string
     */
    private String cutFEN(String fen)
    {
        return fen.substring(0, fen.indexOf(" "));
    }

}
